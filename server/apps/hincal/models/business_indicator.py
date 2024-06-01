from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.hincal.models import Archive
from server.apps.services.base_model import AbstractBaseModel


class BusinessIndicator(AbstractBaseModel):
    """Экономические показатели ИП, физического лица или компании."""

    business = models.ForeignKey(
        'hincal.Business',
        on_delete=models.CASCADE,
        verbose_name=_('Бизнес'),
        related_name='business_indicators',
        db_index=True,
        null=True,
    )
    year = models.PositiveIntegerField(
        _('Год, к которому относятся показатели'),
    )
    average_number_of_staff = models.FloatField(
        _('Среднесписочная численность сотрудников'),
        null=True,
    )
    average_salary_of_staff = models.FloatField(
        _('Средняя заработная плата сотрудника'),
        null=True,
    )
    taxes_to_the_budget = models.FloatField(
        _('Налоги, уплаченные в бюджет Москвы'),
        null=True,
    )
    income_tax = models.FloatField(
        _('Налог на прибыль'),
        null=True,
    )
    property_tax = models.FloatField(
        _('Налог на имущество'),
        null=True,
    )
    land_tax = models.FloatField(
        _('Налог на землю'),
        null=True,
    )
    personal_income_tax = models.FloatField(
        _('НДФЛ'),
        null=True,
    )
    transport_tax = models.FloatField(
        _('Транспортный налог'),
        null=True,
    )
    other_taxes = models.FloatField(
        _('Прочие налоги'),
        null=True,
    )
    
    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Индикатор бизнеса')
        verbose_name_plural = _('Индикаторы бизнесов')
        constraints = [
            models.UniqueConstraint(
                name='unique_year_for_business',
                fields=('year', 'business'),
            ),
        ]

    def __str__(self):
        return f'{self.business}. Год - {self.year}'

    @property
    def actual_archive(self):
        return Archive.objects.get(is_actual=True)

    @property
    def land_area(self) -> float:
        """Возвращаем примерный размер земельного участка."""
        if self.land_tax:
            return (
                self.land_tax /
                (
                    self.actual_archive.land_tax_rate *
                    self.actual_archive.avg_land_cadastral_value
                )
            )
        return 0.0

    @property
    def property_area(self) -> float:
        """Возвращаем примерный размер имущества."""
        if self.property_tax:
            return (
                self.property_tax /
                (
                    self.actual_archive.patent_tax_rate *
                    self.actual_archive.avg_property_cadastral_value
                )
            )
        return 0.0
