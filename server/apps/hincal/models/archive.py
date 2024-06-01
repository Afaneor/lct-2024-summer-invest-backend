from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from server.apps.hincal.services.archive import (
    get_cost_accounting,
    get_registration_costs,
)
from server.apps.services.base_model import AbstractBaseModel


class Archive(AbstractBaseModel):
    """Архив."""

    year = models.PositiveIntegerField(
        _('Год, к которому относятся данные'),
        default=now().year,
    )
    income_tax_rate_to_the_subject_budget = models.FloatField(
        _('Налог на прибыль, уплачиваемый в бюджет субъекта'),
        default=0.18,
    )
    income_tax_rate_to_the_federal_budget = models.FloatField(
        _('Налог на прибыль, уплачиваемый в федеральный бюджет'),
        default=0.02,
    )
    land_tax_rate = models.FloatField(
        _('Размер налоговой ставки на землю'),
        default=0.015,
    )
    property_tax_rate = models.FloatField(
        _('Размер налоговой ставки на имущество'),
        default=0.019,
    )
    patent_tax_rate = models.FloatField(
        _('Размер налоговой ставки по патенту'),
        default=0.06,
    )
    osn_tax_rate = models.FloatField(
        _('Размер налоговой ставки по общей системе налогооблажения'),
        default=0.2,
    )
    ysn_tax_rate = models.FloatField(
        _('Размер налоговой ставки по упрощенной системе налогооблажения'),
        default=0.06,
    )
    personal_income_rate = models.FloatField(
        _('Размер НДФЛ'),
        default=0.13,
    )
    pension_contributions_rate = models.FloatField(
        _('Размер ставки для пенсионных отчислений'),
        default=0.22,
    )
    medical_contributions_rate = models.FloatField(
        _('Размер ставки для медицинских отчислений'),
        default=0.051,
    )
    disability_contributions_rate = models.FloatField(
        _('Размер ставки для по нетрудоспособности'),
        default=0.029,
    )
    lower_margin_error = models.FloatField(
        _('Нижний уровень погрешности для поиска записей'),
        default=0.85,
    )
    upper_margin_error = models.FloatField(
        _('Верхний уровень погрешности для поиска записей'),
        default=1.15,
    )
    cost_accounting = models.JSONField(
        _('Стоимость услуг на ведение бухгалтерского учета'),
        default=get_cost_accounting,
    )
    registration_costs = models.JSONField(
        _('Расходы на регистрацию бизнеса'),
        default=get_registration_costs,
    )
    avg_land_cadastral_value = models.FloatField(
        _('Средняя кадастровая стоимость на землю, тыс. руб.'),
        default=17.23389,
    )
    avg_land_lease_costs = models.FloatField(
        _('Средняя стоимость на аренду земли, тыс. руб.'),
        default=60,
    )
    avg_land_purchase_costs = models.FloatField(
        _('Средняя стоимость на покупку земли, тыс. руб.'),
        default=100,
    )
    avg_property_cadastral_value = models.FloatField(
        _('Средняя кадастровая стоимость на имуществу, тыс. руб.'),
        default=17.23389,
    )
    avg_property_lease_costs = models.FloatField(
        _('Средняя стоимость на аренду имущества, тыс. руб.'),
        default=100,
    )
    avg_property_purchase_costs = models.FloatField(
        _('Средняя стоимость на покупку  имуществу, тыс. руб.'),
        default=200,
    )
    avg_capital_construction_costs = models.FloatField(
        _('Затраты на капитальное строительство, тыс. руб.'),
        default=100,
    )

    is_actual = models.BooleanField(
        _('Актуальные данные в архиве или нет'),
        default=True
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Архив')
        verbose_name_plural = _('Архивы')
        constraints = [
            models.UniqueConstraint(
                name='unique_is_actual_for_archive',
                condition=models.Q(('is_actual', True)),
                fields=('is_actual',)
            ),
        ]

    def __str__(self):
        return f'{self.year}: {self.created_at}'
