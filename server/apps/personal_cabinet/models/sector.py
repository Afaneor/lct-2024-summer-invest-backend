from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class Sector(AbstractBaseModel):
    """Отрасль."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Отрасль')
        verbose_name_plural = _('Отрасли')

    def __str__(self):
        return self.name
