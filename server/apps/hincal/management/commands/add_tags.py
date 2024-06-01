import random
from typing import List

from django.core.management.base import BaseCommand
from django.db.models import Max

from server.apps.blog.models import Post
from server.apps.hincal.models import Equipment, Sector, TerritorialLocation
from server.apps.support.models import Offer, Support


def random_sector(count: int) -> List[str]:
    """Случайный тег сектора."""
    max_id = Sector.objects.all().aggregate(max_id=Max('id'))['max_id']
    sector_tags = []

    while len(sector_tags) != count:
        pk = random.randint(1, max_id)
        sector = Sector.objects.filter(pk=pk).first()
        if sector:
            sector_tags.append(sector.slug)

    return sector_tags


def random_territorial_location(count: int) -> List[str]:
    """Случайный тег территории."""
    max_id = TerritorialLocation.objects.all().aggregate(max_id=Max('id'))['max_id']
    territorial_location_tags = []

    while len(territorial_location_tags) != count:
        pk = random.randint(1, max_id)
        territorial_location = TerritorialLocation.objects.filter(pk=pk).first()
        if territorial_location:
            territorial_location_tags.append(territorial_location.slug)

    return territorial_location_tags


class Command(BaseCommand):
    """Добавление тегов."""

    help = 'Добавление тегов.'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление тегов к сущностям."""
        for offer in Offer.objects.all():
            offer.tags.add(
                *random_sector(15),
                *random_territorial_location(4),
            )
        print('Добавлены теги для Offer')

        for support in Support.objects.all():
            support.tags.add(
                *random_sector(15),
                *random_territorial_location(4),
            )
        print('Добавлены теги для Support')

        for post in Post.objects.all():
            post.tags.add(
                *random_sector(15),
                *random_territorial_location(4),
            )
        print('Добавлены теги для Post')

        for equipment in Equipment.objects.all():
            equipment.tags.add(
                *random_sector(15),
                *random_territorial_location(4),
            )
        print('Добавлены теги для Equipment')
