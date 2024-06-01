from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


# Тип инвестиционной площадка.
# 1 - Технопарк.
# 2 - Технополис.
# 3 - Технополис.
# 4 - Промплощадка
# 5 - Участки для промышленности.
# 6 - КРТ.
class InvestmentSite(AbstractBaseModel):
    """Инвестиционная площадка."""

    investment_site_id = models.IntegerField(
        verbose_name=_('Id объекта'),
    )
    main_photo_url = models.CharField(
        verbose_name=_('Изображение объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    photo_urls = models.JSONField(
        verbose_name=_('Дополнительные изображения'),
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_('Наименование'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    investment_object_type = models.IntegerField(
        verbose_name=_('Тип инвестиционной площадки'),
        null=True,
    )
    detail_url = models.CharField(
        verbose_name=_('Ссылка на investmoscom.ru'),
        blank=True,
    )
    extra_data = models.JSONField(
        verbose_name=_('Дополнительные сведения'),
        null=True,
        blank=True,
    )
    coordinates = models.JSONField(
        blank=True,
        null=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Инвестиционная площадка')
        verbose_name_plural = _('Инвестиционные площадки')

    def __str__(self):
        return self.name
