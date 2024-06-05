from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class TerritorialLocation(AbstractBaseModel):
    """Территориальное расположение."""

    shot_name = models.CharField(
        verbose_name=_('Короткое название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    full_name = models.CharField(
        verbose_name=_('Полное название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    slug = models.SlugField(
        verbose_name=_('Название на английском языке'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Территориальное расположение')
        verbose_name_plural = _('Территориальное расположения')

    def __str__(self):
        return self.full_name
