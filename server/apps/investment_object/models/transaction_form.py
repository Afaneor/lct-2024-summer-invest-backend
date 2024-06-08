from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class TransactionForm(AbstractBaseModel):
    """Форма сделки."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Форма сделки')
        verbose_name_plural = _('Формы транзакций')

    def __str__(self):
        return self.name
