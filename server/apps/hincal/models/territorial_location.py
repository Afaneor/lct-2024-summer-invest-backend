from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class TerritorialLocation(AbstractBaseModel):
    """Территориальное расположение."""

    shot_name = models.CharField(
        _('Короткое название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    full_name = models.CharField(
        _('Полное название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    slug = models.SlugField(
        _('Название на английском языке'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )

    avg_land_cadastral_value = models.FloatField(
        _('Средняя кадастровая стоимость на землю, тыс. руб.'),
        default=18.23389,
    )
    avg_land_lease_costs = models.FloatField(
        _('Средняя стоимость на аренду земли, тыс. руб.'),
        default=1.432,
    )
    avg_land_purchase_costs = models.FloatField(
        _('Средняя стоимость на покупку земли, тыс. руб.'),
        default=91.4233,
    )

    avg_property_cadastral_value = models.FloatField(
        _('Средняя кадастровая стоимость на имуществу, тыс. руб.'),
        default=57.23389,
    )
    avg_property_lease_costs = models.FloatField(
        _('Средняя стоимость на аренду имущества, тыс. руб.'),
        default=2.6314,
    )
    avg_property_purchase_costs = models.FloatField(
        _('Средняя стоимость на покупку  имуществу, тыс. руб.'),
        default=252.231,
    )
    extra_data = models.JSONField(
        _('Дополнительные параметры'),
        null=True,
        blank=True,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Территориальное расположение')
        verbose_name_plural = _('Территориальное расположения')

    def __str__(self):
        return self.full_name
