from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class ServiceProblem(AbstractBaseModel):
    """Сервис проблемы."""

    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    external_category_id = models.CharField(
        verbose_name=_('Id категории проблемы'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    external_subcategory_id = models.CharField(
        verbose_name=_('Id подкатегории проблемы'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    external_theme_id = models.CharField(
        verbose_name=_('Id подкатегории проблемы'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
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
        verbose_name=_('Ссылка на объект'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Сервис проблемы')
        verbose_name_plural = _('Сервис проблем')

    def __str__(self):
        return self.name
