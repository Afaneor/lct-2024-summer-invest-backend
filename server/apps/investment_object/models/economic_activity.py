from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class EconomicActivity(AbstractBaseModel):
    """Экономическая деятельность."""

    code = models.CharField(
        verbose_name=_('Код отрасли'),
        blank=True
    )
    parent_code = models.CharField(
        verbose_name=_('Родительский код отрасли'),
        blank=True
    )
    section = models.CharField(
        verbose_name=_('Секция'),
        blank=True
    )
    name = models.TextField(
        verbose_name=_('Название отрасли'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    comment = models.TextField(
        verbose_name=_('Комментарий'),
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Экономическая деятельность')
        verbose_name_plural = _('Экономические деятельности')

    def __str__(self):
        return self.name
