import logging

from django.core.management.base import BaseCommand

from server.apps.services.parsing.alterainvest import ready_business
from server.apps.services.parsing.torgi_gov import parsing_tender_lot
from server.apps.services.parsing.xlsx.real_estate import parsing_real_estate
from server.apps.services.parsing.xlsx.specialized_site import (
    parsing_specialized_site,
)

logger = logging.getLogger('django')


class Command(BaseCommand):
    """Добавление данных в BusinessIndicator"""

    help = 'Добавление данных в BusinessIndicator'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление данных в BusinessIndicator"""
        # parsing_investmoscow()

        # logger.info('Начался парсинг технополисов и технопарков из файла')
        # parsing_specialized_site()
        # logger.info('Закончился парсинг технополисов и технопарков из файла')
        #
        # logger.info('Начался парсинг зданий и сооружений')
        # parsing_real_estate()
        # logger.info('Закончился парсинг зданий и сооружений')

        logger.info('Начался парсинг тендеров с сайта torgi.gov.ru.')
        parsing_tender_lot()
        logger.info('Закончился парсинг тендеров с сайта torgi.gov.ru.')

        logger.info('Начался парсинг готового бизнеса с сайта alterainvest.ru')
        ready_business()
        logger.info(
            'Закончился парсинг готового бизнеса с сайта alterainvest.ru',
        )
