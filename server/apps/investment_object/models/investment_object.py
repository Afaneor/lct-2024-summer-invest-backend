from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.content_type_id import get_content_type_id
from server.apps.services.enums import ObjectType


class InvestmentObject(AbstractBaseModel):
    """
    Инвестиционный объект.
    """

    name = models.CharField(
        verbose_name=_('Наименование'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
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
    object_type = models.CharField(
        verbose_name=_('Тип объекта'),
        choices=ObjectType.choices,
        default=ObjectType.NOT_DATA,
    )
    economic_activities = models.ManyToManyField(
        to='investment_object.EconomicActivity',
        verbose_name=_('Экономическая деятельность'),
        related_name='investment_objects',
        blank=True,
    )
    transaction_form = models.ForeignKey(
        to='investment_object.TransactionForm',
        verbose_name=_('Форма сделки'),
        on_delete=models.CASCADE,
        related_name='investment_objects',
    )
    cost = models.FloatField(
        verbose_name=_('Стоимость'),
        null=True,
    )
    land_area = models.FloatField(
        verbose_name=_('Площадь земли'),
        null=True,
    )
    building_area = models.FloatField(
        verbose_name=_('Площадь помещений'),
        null=True,
    )
    location = models.CharField(
        verbose_name=_('Местоположение'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    url = models.CharField(
        verbose_name=_('Ссылка на объект'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    longitude = models.DecimalField(
        verbose_name=_('Долгота'),
        decimal_places=3,
        max_digits=9,
        null=True,
    )
    latitude = models.DecimalField(
        verbose_name=_('Широта'),
        decimal_places=3,
        max_digits=9,
        null=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Инвестиционный объект')
        verbose_name_plural = _('Инвестиционные объекты')
        constraints = [
            models.CheckConstraint(
                name='object_type_valid',
                check=models.Q(object_type__in=ObjectType.values),
            ),
        ]

    def __str__(self):
        return self.name

    @property
    def content_type_id(self) -> int:
        """Content type id утечки."""
        return get_content_type_id(self)
