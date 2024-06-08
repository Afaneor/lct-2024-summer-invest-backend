from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class SpecializedSite(AbstractBaseModel):
    """Специализированная площадка."""

    investment_object = models.OneToOneField(
        to='investment_object.InvestmentObject',
        verbose_name=_('Специализированная площадка'),
        on_delete=models.CASCADE,
        related_name='specialized_site'
    )
    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    sez = models.CharField(
        verbose_name=_('Особая экономическая зона'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    tad = models.CharField(
        verbose_name=_('Территория опережающего развития'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    region = models.CharField(
        verbose_name=_('Регион'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    nearest_cities = models.CharField(
        verbose_name=_('Ближайшие города'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    number_residents = models.IntegerField(
        verbose_name=_('Количество резидентов'),
        blank=True,
        null=True,
    )
    document_url = models.CharField(
        verbose_name=_('Документы по объекту'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    year_formation = models.IntegerField(
        verbose_name=_('Год формирования объекта'),
        blank=True,
        null=True,
    )
    validity = models.IntegerField(
        verbose_name=_('Срок действия объекта'),
        blank=True,
        null=True,
    )
    restrictions = models.ManyToManyField(
        to='investment_object.Restriction',
        verbose_name=_('Ограничения по видам деятельности'),
        related_name='specialized_sites',
        blank=True,
    )
    infrastructures = models.ManyToManyField(
        to='investment_object.Infrastructure',
        verbose_name=_('Инфрастуктура'),
        related_name='specialized_sites',
        blank=True,
    )
    additional_services = models.CharField(
        verbose_name=_('Дополнительные услуги управляющей компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    object_administrator_name = models.CharField(
        verbose_name=_('Название администратора объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    address = models.CharField(
        verbose_name=_('Адрес администратора объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    working_hours = models.CharField(
        verbose_name=_('Время работы'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    income_tax = models.CharField(
        verbose_name=_('Налог на прибыль'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    property_tax = models.CharField(
        verbose_name=_('Налог на имущество'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    land_tax = models.CharField(
        verbose_name=_('Земельный налог'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    transport_tax = models.CharField(
        verbose_name=_('Транспортный налог'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    insurance_premiums = models.CharField(
        verbose_name=_('Страховые взносы'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    privileges = models.ManyToManyField(
        to='investment_object.Privilege',
        verbose_name=_('Льготы'),
        related_name='specialized_sites',
        blank=True,
    )
    is_free_customs_zone_regime = models.CharField(
        verbose_name=_('Наличие режима свободной таможенной зоны'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    resident_info = models.TextField(
        verbose_name=_('Информация о том, как стать новым резидентом'),
        blank=True,
    )
    minimum_investment_amount = models.CharField(
        verbose_name=_('Минимальный объем инвестиций'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    urban_planning = models.CharField(
        verbose_name=_('Градостроительные характеристики и ограничения'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Специализированная площадка')
        verbose_name_plural = _('Специализированные площадки')

    def __str__(self):
        return self.investment_object
