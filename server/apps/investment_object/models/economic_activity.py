from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class EconomicActivity(AbstractBaseModel):
    """Экономическая деятельность."""

    code = models.CharField(
        verbose_name=_('Код отрасли'),
        unique=True,
    )
    name = models.CharField(
        verbose_name=_('Название отрасли'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Экономическая деятельность')
        verbose_name_plural = _('Экономические деятельности')

    def __str__(self):
        return f'{self.code} - {self.name}'
