import logging

from django.core.management.base import BaseCommand

from server.apps.services.parsing.investmoscow.problem import parsing_problem

logger = logging.getLogger('django')


class Command(BaseCommand):
    """Добавление данных для поддержки."""

    help = 'Добавление данных в BusinessIndicator'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление данных в BusinessIndicator"""
        # parsing_investmoscow()

        logger.info('Начался парсинг проблем с сайта investmoscow.ru')
        parsing_problem()
        logger.info('Закончился парсинг проблем с сайта investmoscow.ru')
