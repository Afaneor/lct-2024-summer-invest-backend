import datetime
import logging
import os

from django.conf import settings
from docxtpl import DocxTemplate

from server.settings.components.common import MEDIA_ROOT

logger = logging.getLogger(__name__)


def get_document():
    """Получение шаблона."""
    document = DocxTemplate(
        (
            f'{settings.BASE_DIR}/server/templates/report/' +
            f'report.docx'
        ),
    )

    return document


def create_selection_request_report(
    now_dt: str,
) -> bool:
    """Формирование отчета."""
    document = get_document()
    # Формируем данные.
    generated_data = []
    document.render({'generated_data': generated_data})
    document.save(
        os.path.join(
            MEDIA_ROOT,
            f'{now_dt}.docx',
        ),
    )
    logger.info(f'Конец: {datetime.datetime.now()}')
    return True
