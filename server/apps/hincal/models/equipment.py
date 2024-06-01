from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class Equipment(AbstractBaseModel):
    """Оборудование."""

    name = models.CharField(
        _('Название оборудования'),
        unique=True,
    )
    cost = models.FloatField(
        _('Стоимость оборудования'),
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудования')

    def __str__(self):
        return f'{self.name}'
