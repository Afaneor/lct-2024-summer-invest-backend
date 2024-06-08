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
    bidding_type = models.CharField(
        verbose_name=_('Вид торгов'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    tender_lot_id = models.CharField(
        verbose_name=_('Id лота тендера'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_('Название лота'),
        blank=True,
    )
    extra_data = models.JSONField(
        verbose_name=_('Дополнительные сведения'),
        null=True,
        blank=True,
    )
    url = models.CharField(
        verbose_name=_('Ссылка на torgi.gov.ru'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Лот тендера')
        verbose_name_plural = _('Лоты тендера')

    def __str__(self):
        return str(self.investment_object)
