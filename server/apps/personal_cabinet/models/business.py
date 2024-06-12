from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.enums import BusinessType, TaxSystemType
from server.apps.services.validators import inn_validator


class Business(AbstractBaseModel):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='businesses',
        db_index=True,
        null=True,
    )
    position = models.CharField(
        verbose_name=_('Должность пользователя в бизнесе'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    business_type = models.CharField(
        verbose_name=_('Тип бизнеса'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=BusinessType.choices,
        blank=True,
    )
    inn = models.CharField(
        verbose_name=_('ИНН физического лица, ИП или компания'),
        max_length=12,  # noqa: WPS432
        validators=[inn_validator],
        blank=True,
    )
    sector = models.ForeignKey(
        to='personal_cabinet.Sector',
        on_delete=models.CASCADE,
        verbose_name=_('Отрасль хозяйственной деятельности'),
        related_name='businesses',
        null=True,
    )
    sub_sector = models.ForeignKey(
        to='personal_cabinet.SubSector',
        on_delete=models.CASCADE,
        verbose_name=_('Подотрасль хозяйственной деятельности'),
        related_name='business',
        null=True,
    )
    territorial_location = models.ForeignKey(
        to='personal_cabinet.TerritorialLocation',
        on_delete=models.CASCADE,
        verbose_name=_('Территориальное положение бизнеса'),
        related_name='businesses',
        null=True,
        blank=True,
    )
    # Основная информация по бизнесу.
    hid = models.CharField(
        verbose_name=_('Уникальный id контрагента в dadata'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    short_business_name = models.CharField(
        verbose_name=_('Короткое название ИП или компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    full_business_name = models.CharField(
        verbose_name=_('Полное название ИП или компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    management_name = models.CharField(
        verbose_name=_('ФИО руководителя, только для компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    management_position = models.CharField(
        verbose_name=_('Должность руководителя, только для компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    full_opf = models.CharField(
        verbose_name=_('Полное наименование правовой формы'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    short_opf = models.CharField(
        verbose_name=_('Короткое наименование правовой формы'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    okved = models.CharField(
        verbose_name=_('ОКВЕД'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    # Если ИП, то будет ФИО
    first_name = models.CharField(
        verbose_name=_('Имя'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_('Фамилия'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    middle_name = models.CharField(
        verbose_name=_('Отчество'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    # Данные по адресу.
    address = models.CharField(
        verbose_name=_('Полный адрес'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    country = models.CharField(
        verbose_name=_('Страна'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    region = models.CharField(
        verbose_name=_('Город'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    city_area = models.CharField(
        verbose_name=_('Область, округ'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    city_district = models.CharField(
        verbose_name=_('Район'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    # Контактная информация.
    phone = models.CharField(
        verbose_name=_('Телефон, относящийся к бизнесу'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_('Email, относящийся к бизнесу'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    site = models.CharField(
        verbose_name=_('Сайт, относящийся к бизнесу'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    tax_system_type = models.CharField(
        verbose_name=_('Тип системы налогооблажения'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=TaxSystemType.choices,
        default=TaxSystemType.OSN,
    )
    economic_activities = models.ManyToManyField(
        to='investment_object.EconomicActivity',
        verbose_name=_('Экономическая деятельность'),
        related_name='business',
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Бизнес')
        verbose_name_plural = _('Бизнесы')
        constraints = [
            models.CheckConstraint(
                name='business_type_valid',
                check=models.Q(business_type__in=[*BusinessType.values, '']),
            ),
            models.CheckConstraint(
                name='tax_system_type_valid',
                check=models.Q(tax_system_type__in=TaxSystemType.values),
            ),
        ]

    def __str__(self):
        return f'{self.business_type} - {self.user}. ИНН - {self.inn}'
