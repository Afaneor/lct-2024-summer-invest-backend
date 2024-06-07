from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class ProblemReport(AbstractBaseModel):
    """Сообщение о проблеме."""

    external_id = models.IntegerField(
        verbose_name=_('Id проблемы на investmoscom.ru'),
    )
    external_category_id = models.IntegerField(
        verbose_name=_('Id категории проблемы на investmoscom.ru'),
    )
    external_subcategory_id = models.IntegerField(
        verbose_name=_('Id подкатегории проблемы на investmoscom.ru'),
    )
    external_theme_id = models.IntegerField(
        verbose_name=_('Id подкатегории проблемы на investmoscom.ru'),
    )
    name = models.TextField(
        verbose_name=_('Название проблемы'),
    )
    category_name = models.CharField(
        verbose_name=_('Название категории'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    subcategory_name = models.CharField(
        verbose_name=_('Название подкатегории'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    theme_name = models.CharField(
        verbose_name=_('Название темы'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    additional_info = models.TextField(
        verbose_name=_('Дополнительная информация'),
        blank=True,
    )
    url = models.CharField(
        verbose_name=_('Дополнительная информация'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Сообщение о проблеме')
        verbose_name_plural = _('Сообщения о проблемах')

    def __str__(self):
        return self.name
