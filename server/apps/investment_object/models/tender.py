from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Tender(AbstractBaseModel):
    """Тендер."""

    tender_id = models.CharField(
        verbose_name=_('Id тендера'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    bidding_type = models.CharField(
        verbose_name=_('Вид торгов'),
        max_length=settings.MAX_STRING_LENGTH,
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
        verbose_name = _('Тендер')
        verbose_name_plural = _('Тендеры')

    def __str__(self):
        return self.tender_id
