from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class InfrastructureAvailability(models.TextChoices):

    POSSIBLE_CREATION = 'possible_creation'
    YES = 'yes'


class Infrastructure(AbstractBaseModel):
    """Инфраструктура."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    consumption_tariff = models.CharField(
        verbose_name=_('Тариф на потребление'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True
    )
    transportation_tariff = models.CharField(
        verbose_name=_('Тариф на транспортировку'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True
    )
    max_allowable_power = models.CharField(
        verbose_name=_('Максимально допустимая мощность'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True
    )
    free_power = models.CharField(
        verbose_name=_('Свободная мощность'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True
    )
    throughput = models.CharField(
        verbose_name=_('Пропускная способность'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True
    )
    other_characteristics = models.TextField(
        verbose_name=_('Иные характеристики'),
        blank=True,
    )
    availability = models.CharField(
        verbose_name=_('Наличие'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Инфраструктура')
        verbose_name_plural = _('Инфраструктуры')

    def __str__(self):
        return self.name
