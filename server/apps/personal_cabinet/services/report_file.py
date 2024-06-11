import io
from abc import ABC, abstractmethod
from typing import Any, Dict

from django.conf import settings
from docxtpl import DocxTemplate

from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.personal_cabinet.services.pdf_converter import (
    DocumentConverter,
)


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
        """Рендеринг документа и перевод его в pdf."""
        document = DocxTemplate(template_full_path)
        document.render(context)
        file_stream = io.BytesIO()
        document.save(file_stream)
        file_stream.seek(0)
        content = DocumentConverter.convert_docx_to_pdf(file_stream)

        return io.BytesIO(content)


class SelectionRequestFile(object):  # noqa: WPS214
    """Генерация отчета для запроса на подбор."""

    # Рендеринг документов исходя из форматов.
    _render_handlers = {
        'docx': RenderDocx(),
    }

    def __init__(
        self,
        document_format: str,
        selection_request: SelectionRequest,
    ) -> None:
        """Инициализируем переменные для работы."""
        self.document_format = document_format
        self.selection_request = selection_request

    def get_template_full_path(self) -> str:
        """Получение шаблона для создания документа."""
        return (
            f'{settings.BASE_DIR}/server/templates/selection_request/' +
            f'invest.{self.document_format}'
        )

    def get_file_name(self) -> str:
        """Получение корректного названия документа."""
        return 'Отчет_на_подбор_инвестиционных объектов_{id}'.format(
            id=self.selection_request.id,
        )

    def generate(self) -> io.BytesIO:
        """Генерация документа."""
        context = formation_context(selection_request=self.selection_request)

        return self._render_handlers.get(self.document_format).render(
            context=context,
            template_full_path=self.get_template_full_path(),
            file_name=self.get_file_name(),
        )


def formation_context(selection_request: SelectionRequest) -> Dict[str, Any]:
    """Формирование контекста для файла."""
    return {}
