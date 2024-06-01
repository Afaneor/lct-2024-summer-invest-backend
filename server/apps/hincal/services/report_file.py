import io
import json
from abc import ABC, abstractmethod

import requests
from django.conf import settings
from docxtpl import DocxTemplate, Listing

from server.apps.hincal.models import Report


class AbstractRender(ABC):  # noqa: B024
    """Абстрактный класс для рендеринга документов."""

    def __init__(self, *args, **kwargs) -> None:  # noqa: B027
        """Инициализируем переменные для работы."""
        pass  # noqa: WPS420

    @abstractmethod
    def render(
        self,
        context: dict,  # type: ignore
        template_full_path: str,
        file_name: str,
    ) -> io.BytesIO:
        """Рендеринг документа."""
        pass  # noqa: WPS420


class RenderDocx(AbstractRender):
    """Рендеринг docx-документов."""

    def render(
        self,
        context: dict,  # type: ignore
        template_full_path: str,
        file_name: str,
    ) -> io.BytesIO:
        """Рендеринг документа."""
        document = DocxTemplate(template_full_path)
        document.render(context)
        document.save(f'{settings.MEDIA_ROOT}/{file_name}.docx')

        # https://pspdfkit.com/api/pdf-generator-api
        instructions = {'parts': [{'file': 'document'}]}

        response = requests.request(
            'POST',
            'https://api.pspdfkit.com/build',
            headers={
                'Authorization': f'Bearer {settings.PSPDFKIT_API_SECRET_KEY}',
            },
            files={
                'document':
                    open(f'{settings.MEDIA_ROOT}/{file_name}.docx', 'rb'),
            },
            data={'instructions': json.dumps(instructions)},
            stream=True,
        )

        if response.ok:
            with open(f'{settings.MEDIA_ROOT}/{file_name}.pdf', 'wb') as report:
                for chunk in response.iter_content(chunk_size=8096):  # noqa: WPS432, E501
                    report.write(chunk)
        else:
            # Если не доступно, то отправляем docx.
            with open(f'{settings.MEDIA_ROOT}/{file_name}.docx', 'rb') as report:  # noqa: E501
                buffer = io.BytesIO(report.read())
                buffer.seek(0)
                return buffer
        # Если доступно, то отправляем pdf.
        with open(f'{settings.MEDIA_ROOT}/{file_name}.pdf', 'rb') as report:
            buffer = io.BytesIO(report.read())
            buffer.seek(0)
            return buffer


class ReportFile(object):  # noqa: WPS214
    """Генерация отчета."""

    # Рендеринг документов исходя из форматов.
    _render_handlers = {
        'docx': RenderDocx(),
        'doc': RenderDocx(),
    }

    def __init__(
        self,
        document_format: str,
        report: Report,
    ) -> None:
        """Инициализируем переменные для работы."""
        self.document_format = document_format
        self.report = report

    def get_template_full_path(self) -> str:
        """Получение шаблона для создания документа."""
        return (
            f'{settings.BASE_DIR}/server/templates/report/' +
            f'report.{self.document_format}'
        )

    def get_file_name(self) -> str:
        """Получение корректного названия документа."""
        return 'Отчет_{id}'.format(id=self.report.id)

    def generate(self) -> io.BytesIO:
        """Генерация документа."""
        return self._render_handlers.get(self.document_format).render(
            context=self.report.context.get('context_for_file'),
            template_full_path=self.get_template_full_path(),
            file_name=self.get_file_name(),
        )
