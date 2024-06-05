from django.core.management.base import BaseCommand

from server.apps.investment_object.services.parsing.website.torgi_gov import (
    parsing_tender,
)


class Command(BaseCommand):
    """Добавление данных в BusinessIndicator"""

    help = 'Добавление данных в BusinessIndicator'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление данных в BusinessIndicator"""
        # parsing_investment_site()
        parsing_tender()
