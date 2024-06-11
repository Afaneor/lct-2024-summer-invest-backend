import logging
import pprint

import requests
from django.conf import settings
from requests import RequestException

logger = logging.getLogger(__name__)


class DocumentConverter:
    """Конвертер документов в pdf формат."""

    office_convert_url = settings.DOCUMENT_CONVERTER_URL + '/convert/office'

    @classmethod
    def convert_docx_to_pdf(cls, file: bytes):
        """Конвертирование содержимого docx файла в содержимое pdf файла."""
        files = {'file': ('report.docx', file)}
        try:
            response = requests.post(
                cls.office_convert_url,
                files=files,
                timeout=30,
            )
            response.raise_for_status()
        except RequestException as exc:
            raise
        return response.content
