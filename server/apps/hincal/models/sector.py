from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.hincal.services.archive import (
    get_average_salary_of_staff,
    get_possible_income_from_patent,
    get_possible_income_on_market,
)
from server.apps.services.base_model import AbstractBaseModel


class Sector(AbstractBaseModel):
    """Отрасль."""

    name = models.CharField(
        _('Название'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    slug = models.SlugField(
        _('Название на английском языке'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    possible_income_from_patent = models.JSONField(
        _('Возможный доход по патентной системе налогообложения, тыс. руб.'),
        default=get_possible_income_from_patent,
    )
    possible_income_on_market = models.JSONField(
        _('Возможный доход, тыс. руб.'),
        default=get_possible_income_on_market,
    )
    average_salary_of_staff = models.JSONField(
        _('Средняя заработная плата сотрудника, тыс. руб.'),
        default=get_average_salary_of_staff,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Отрасль')
        verbose_name_plural = _('Отрасли')

    def __str__(self):
        return self.name
