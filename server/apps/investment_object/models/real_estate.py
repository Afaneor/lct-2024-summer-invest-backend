from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class RealEstate(AbstractBaseModel):
    """Недвижимость."""

    investment_object = models.OneToOneField(
        to='investment_object.InvestmentObject',
        verbose_name=_('Специализированная площадка'),
        on_delete=models.CASCADE,
        related_name='real_estate'
    )
    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    preferential_treatment = models.CharField(
        verbose_name=_('Преференциальный режим'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    preferential_treatment_object_code = models.CharField(
        verbose_name=_('Код объекта преференциального режима'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    preferential_treatment_object_name = models.CharField(
        verbose_name=_('Наименование объекта преференциального режима'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    support_infrastructure_object = models.CharField(
        verbose_name=_('Объект инфраструктуры поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    support_infrastructure_object_code = models.CharField(
        verbose_name=_('Код объекта инфраструктуры поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    support_infrastructure_object_name = models.CharField(
        verbose_name=_('Наименование объекта инфраструктуры поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    region = models.CharField(
        verbose_name=_('Регион'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    address = models.CharField(
        verbose_name=_('Адрес администратора объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    nearest_cities = models.CharField(
        verbose_name=_('Ближайшие города'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    site_format = models.CharField(
        verbose_name=_('Формат площадки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    site_type = models.CharField(
        verbose_name=_('Тип площадки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    ownership_type = models.CharField(
        verbose_name=_('Тип собственности'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    rental_period = models.CharField(
        verbose_name=_('Сроки аренды'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    procedure_determining_cost = models.CharField(
        verbose_name=_('Порядок определения стоимости'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    hazard_class_object = models.CharField(
        verbose_name=_('Класс опасности объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    characteristic_object = models.TextField(
        verbose_name=_('Характеристики расположенных объектов капитального строительства'),
        blank=True,
    )
    land_cadastral_number = models.CharField(
        verbose_name=_('Свободная площадь ЗУ, га'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    permitted_use_options = models.CharField(
        verbose_name=_('Варианты разрешенного использования'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    cupping = models.CharField(
        verbose_name=_('Возможность мезжевания'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    land_category = models.CharField(
        verbose_name=_('Категория земель'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    building_cadastral_number = models.CharField(
        verbose_name=_('Кадастровый номер здания, сооружения, помещения'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    building_technical_specifications = models.CharField(
        verbose_name=_('Технические характеристики здания, сооружения, помещения'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    owner_name = models.CharField(
        verbose_name=_('Наименование собственника / администратора объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    owner_inn = models.CharField(
        verbose_name=_('ИНН собственника'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    other_characteristics = models.TextField(
        verbose_name=_('Иные характеристики'),
        blank=True,
    )
    application_procedure = models.TextField(
        verbose_name=_('Описание процедуры подачи заявки'),
        blank=True,
    )
    documents_for_application = models.TextField(
        verbose_name=_('Перечень документов, необходимых для подачи заявки'),
        blank=True,
    )
    application_form_url = models.TextField(
        verbose_name=_('Ссылка на форму подачи заявки'),
        blank=True,
    )
    urban_planning = models.TextField(
        verbose_name=_('Градостроительные характеристики и ограничения'),
        blank=True,
    )
    other_information = models.TextField(
        verbose_name=_('Иные сведения'),
        blank=True,
    )
    maip = models.CharField(
        verbose_name=_('Наличие МАИП'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    benefit_description = models.TextField(
        verbose_name=_('Описание льготы'),
        blank=True,
    )
    infrastructures = models.ManyToManyField(
        to='investment_object.Infrastructure',
        verbose_name=_('Инфрастуктура'),
        related_name='real_estates',
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Недвижимость')
        verbose_name_plural = _('Недвижимости')

    def __str__(self):
        return str(self.investment_object)
