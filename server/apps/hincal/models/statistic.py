from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Statistic(AbstractBaseModel):
    """Статистика."""

    year = models.PositiveIntegerField(
        _('Год, к которому относятся показатели'),
    )
    sector = models.ForeignKey(
        'hincal.Sector',
        on_delete=models.CASCADE,
        verbose_name=_('Сектор'),
        related_name='statistics',
        db_index=True,
    )
    volume_of_sales = models.FloatField(
        _('Объем реализации, тыс. руб.'),
        null=True,
    )
    growth_rate = models.FloatField(
        _('Темп роста выручки за год'),
        null=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Статистика')
        verbose_name_plural = _('Статистики')
        constraints = [
            models.UniqueConstraint(
                name='unique_year_for_sector_statistic',
                fields=('year', 'sector'),
            ),
        ]

    def __str__(self):
        return f'{self.year}: {self.sector}'
