from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class ReadyBusiness(AbstractBaseModel):
    """Готовый бизнес."""

    investment_object = models.OneToOneField(
        to='investment_object.InvestmentObject',
        verbose_name=_('Специализированная площадка'),
        on_delete=models.CASCADE,
        related_name='ready_business'
    )
    external_id = models.IntegerField(
        verbose_name=_('Id объекта на alterainvest.ru'),
        null=True,
    )
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )
    extra_data = models.JSONField(
        verbose_name=_('Дополнительные сведения с alterainvest.ru'),
        null=True,
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Готовый бизнес')
        verbose_name_plural = _('Готовые бизнесы')

    def __str__(self):
        return self.name
