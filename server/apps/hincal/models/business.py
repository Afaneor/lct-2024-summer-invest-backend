from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.hincal.services.enums import TypeBusiness, TypeTaxSystem
from server.apps.hincal.services.validators import inn_validator
from server.apps.services.base_model import AbstractBaseModel


class Business(AbstractBaseModel):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """
    
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='businesses',
        db_index=True,
        null=True,
    )
    position = models.CharField(
        _('Должность пользователя в бизнесе'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    type = models.CharField(
        _('Тип бизнеса'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=TypeBusiness.choices,
        blank=True,
    )
    inn = models.CharField(
        _('ИНН физического лица, ИП или компания'),
        max_length=12,  # noqa: WPS432
        validators=[inn_validator],
        blank=True,
    )
    sector = models.ForeignKey(
        'hincal.Sector',
        on_delete=models.CASCADE,
        verbose_name=_('Отрасль хозяйственной деятельности'),
        related_name='businesses',
    )
    sub_sector = models.ForeignKey(
        'hincal.SubSector',
        on_delete=models.CASCADE,
        verbose_name=_('Подотрасль хозяйственной деятельности'),
        related_name='business',
    )
    territorial_location = models.ForeignKey(
        'hincal.TerritorialLocation',
        on_delete=models.CASCADE,
        verbose_name=_('Территориальное положение бизнеса'),
        related_name='businesses',
        null=True,
        blank=True,
    )
    # Основная информация по бизнесу.
    hid = models.CharField(
        _('Уникальный id контрагента в dadata'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    short_business_name = models.CharField(
        _('Короткое название ИП или компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    full_business_name = models.CharField(
        _('Полное название ИП или компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    management_name = models.CharField(
        _('ФИО руководителя, только для компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    management_position = models.CharField(
        _('Должность руководителя, только для компании'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    full_opf = models.CharField(
        _('Полное наименование правовой формы'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    short_opf = models.CharField(
        _('Короткое наименование правовой формы'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    okved = models.CharField(
        _('ОКВЕД'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    # Если ИП, то будет ФИО
    first_name = models.CharField(
        _('Имя'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    last_name = models.CharField(
        _('Фамилия'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    middle_name = models.CharField(
        _('Отчество'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    # Данные по адресу.
    address = models.CharField(
        _('Полный адрес'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    country = models.CharField(
        _('Страна'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    region = models.CharField(
        _('Город'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    city_area = models.CharField(
        _('Область, округ'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    city_district = models.CharField(
        _('Район'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    # Контактная информация.
    phone = models.CharField(
        _('Телефон, относящийся к бизнесу'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    email = models.EmailField(
        _('Email, относящийся к бизнесу'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    site = models.CharField(
        _('Сайт, относящийся к бизнесу'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    type_tax_system = models.CharField(
        _('Тип системы налогооблажения'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=TypeTaxSystem.choices,
        default=TypeTaxSystem.OSN,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Бизнес')
        verbose_name_plural = _('Бизнесы')
        constraints = [
            models.CheckConstraint(
                name='type_valid',
                check=models.Q(type__in=[*TypeBusiness.values, '']),
            ),
            models.CheckConstraint(
                name='type_tax_system_valid',
                check=models.Q(type_tax_system__in=TypeTaxSystem.values),
            ),
        ]

    def __str__(self):
        return f'{self.type} - {self.user}. ИНН - {self.inn}'
