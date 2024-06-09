from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.enums import TransactionFormType


class TransactionForm(AbstractBaseModel):
    """Форма сделки."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    transaction_form_type = models.CharField(
        verbose_name=_('Тип сделки'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=TransactionFormType.choices,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Форма сделки')
        verbose_name_plural = _('Формы транзакций')
        constraints = [
            models.CheckConstraint(
                name='transaction_form_type_valid',
                check=models.Q(
                    transaction_form_type__in=TransactionFormType.values,
                ),
            ),
        ]

    def __str__(self):
        return self.name
