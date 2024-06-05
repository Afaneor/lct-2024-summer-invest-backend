from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


# Тип инвестиционной площадка.
# 1 - Технопарк.
# 2 - Технополис.
# 3 - Земля.
# 4 - Промплощадка
# 5 - Участки для промышленности.
# 6 - КРТ.
class InvestmentObject(AbstractBaseModel):
    """
    Инвестиционный объект.
    """

    external_id = models.IntegerField(
        verbose_name=_('Id объекта на investmoscom.ru'),
        null=True,
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
    object_type = models.IntegerField(
        verbose_name=_('Тип объекта'),
        null=True,
    )
    url = models.CharField(
        verbose_name=_('Ссылка на investmoscom.ru'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    extra_data = models.JSONField(
        verbose_name=_('Дополнительные сведения с investmoscom.ru'),
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        verbose_name=_('Долгота'),
        decimal_places=3,
        max_digits=9,
    )
    latitude = models.DecimalField(
        verbose_name=_('Широта'),
        decimal_places=3,
        max_digits=9,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Инвестиционный объект')
        verbose_name_plural = _('Инвестиционные объекты')

    def __str__(self):
        return self.name
