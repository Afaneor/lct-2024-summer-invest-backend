import logging

from django.core.management.base import BaseCommand

from server.apps.investment_object.services.parsing.alterainvest import (
    parsing_ready_business,
)
from server.apps.investment_object.services.parsing.torgi_gov import (
    parsing_tender,
)
from server.apps.investment_object.services.parsing.xlsx_file import (
    parsing_real_estate,
    parsing_specialized_site,
    parsing_support,
)

logger = logging.getLogger('django')


class Command(BaseCommand):
    """Добавление данных в BusinessIndicator"""

    help = 'Добавление данных в BusinessIndicator'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление данных в BusinessIndicator"""
        # parsing_investmoscow()

        logger.info('Начался парсинг технополисов и технопарков из файла')
        parsing_specialized_site()
        logger.info('Закончился парсинг технополисов и технопарков из файла')

        logger.info('Начался парсинг зданий и сооружений')
        parsing_real_estate()
        logger.info('Закончился парсинг зданий и сооружений')

        logger.info('Начался парсинг мер поддержки')
        parsing_support()
        logger.info('Закончился парсинг мер поддержки')

        logger.info('Начался парсинг тендеров с сайта torgi.gov.ru.')
        parsing_tender()
        logger.info('Закончился парсинг тендеров с сайта torgi.gov.ru.')

        logger.info('Начался парсинг готового бизнеса с сайта alterainvest.ru')
        parsing_ready_business()
        logger.info(
            'Закончился парсинг готового бизнеса с сайта alterainvest.ru',
        )
