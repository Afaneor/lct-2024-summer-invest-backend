import logging

from django.core.management.base import BaseCommand

from server.apps.services.parsing.investmoscow.problem_report import (
    parsing_problem_report,
)
from server.apps.services.parsing.investmoscow.service_support import (
    parsing_service_support,
)
from server.apps.services.parsing.xlsx.service_support import parsing_service_support

logger = logging.getLogger('django')


class Command(BaseCommand):
    """Добавление данных для поддержки."""

    help = 'Добавление данных в BusinessIndicator'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление данных в BusinessIndicator"""
        logger.info(
            'Начался парсинг данных о проблемах с сайта investmoscow.ru',
        )
        parsing_problem_report()
        logger.info(
            'Закончился парсинг данных о проблемах с сайта investmoscow.ru',
        )

        # logger.info(
        #     'Начался парсинг каталога сервисов с сайта investmoscow.ru',
        # )
        # parsing_service_support()
        # logger.info(
        #     'Закончился парсинг каталога сервисов с сайта investmoscow.ru',
        # )

        logger.info('Начался парсинг мер поддержки')
        parsing_service_support()
        logger.info('Закончился парсинг мер поддержки')
