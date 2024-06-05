from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class SubSector(AbstractBaseModel):
    """Подотрасль."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_('Название на английском языке'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Подотрасль')
        verbose_name_plural = _('Подотрасли')

    def __str__(self):
        return self.name
