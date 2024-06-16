import io
from abc import ABC, abstractmethod
from typing import Any, Dict

from django.conf import settings
from django.db import models
from django.db.models import CharField
from django.db.models.functions import Concat
from docxtpl import DocxTemplate

from server.apps.investment_object.models import InvestmentObject
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.personal_cabinet.services.pdf_converter import (
    DocumentConverter,
)
from server.apps.services.enums import ObjectType
from server.apps.support.models import ServiceSupport


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
    # summary = MessageService().get_summary(selection_request)
    investment_object_filters = {}
    service_support_filters = {}
    for message in selection_request.messages.all():
        if message.bot_filter and message.bot_filter.get('investment_object'):
            investment_object_filters.update(
                message.bot_filter.get('investment_object'),
            )
        if message.bot_filter and message.bot_filter.get('service_support'):
            service_support_filters.update(
                message.bot_filter.get('service_support'),
            )

    # Объекты InvestmentObject для отчета.
    investment_objects = InvestmentObject.objects.filter(
        **investment_object_filters,
    ).annotate(
        url_to_front=Concat(
            models.Value('https://prod.invest.yapa.one/smart-assistant/'),
            models.F('id'),
            models.Value('/'),
            output_field=CharField(),
        ),
    ).values(
        'name',
        'object_type',
        'cost',
        'location',
        'transaction_form__name',
        'land_area',
        'building_area',
        'url_to_front',
    )[:5]

    # Объекты ServiceSupport для отчета.
    service_supports = ServiceSupport.objects.filter(
        **service_support_filters,
    ).annotate(
        url_to_front=Concat(
            models.Value('https://prod.invest.yapa.one/supports/'),
            models.F('id'),
            models.Value('/'),
            output_field=CharField(),
        ),
    ).values(
        'name',
        'support_type',
        'url_to_front',
    )[:5]

    for investment_object in investment_objects:
        investment_object.update(
            {
                'object_type':
                    dict(ObjectType.choices).get(
                        investment_object.get('object_type'),
                    ),
                'cost': (
                    f'{investment_object.get("cost")} руб.'
                    if investment_object.get('cost')
                    else '-'
                ),
                'location': (
                    investment_object.get('location')
                    if investment_object.get('location')
                    else '-'
                ),
                'transaction_form__name': (
                    investment_object.get('transaction_form__name')
                    if investment_object.get('transaction_form__name')
                    else '-'
                ),
                'land_area': (
                    investment_object.get('land_area')
                    if investment_object.get('land_area')
                    else '-'
                ),
                'building_area': (
                    investment_object.get('building_area')
                    if investment_object.get('building_area')
                    else '-'
                ),
            }
        )

    return {
        'investment_objects': investment_objects,
        'service_supports': service_supports,
        # 'summary': summary,
    }
