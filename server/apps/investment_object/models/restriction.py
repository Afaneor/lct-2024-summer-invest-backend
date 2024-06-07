from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Restriction(AbstractBaseModel):
    """Ограничения по видам деятельности."""

    name = models.TextField(
        verbose_name=_('Название'),
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Ограничение по видам деятельности')
        verbose_name_plural = _('Ограничения по видам деятельности')

    def __str__(self):
        return f'{self.name}'
