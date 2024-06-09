from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class TenderLot(AbstractBaseModel):
    """Лот тендера."""

    investment_object = models.OneToOneField(
        to='investment_object.InvestmentObject',
        verbose_name=_('Специализированная площадка'),
        on_delete=models.CASCADE,
        related_name='tender_lot'
    )
    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        blank=True,
    )
    extra_data = models.JSONField(
        verbose_name=_('Дополнительные сведения'),
        null=True,
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Лот тендера')
        verbose_name_plural = _('Лоты тендера')

    def __str__(self):
        return str(self.investment_object)
