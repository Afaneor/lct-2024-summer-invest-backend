from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class Report(AbstractBaseModel):
    """Отчет."""

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='reports',
        db_index=True,
        null=True,
    )
    initial_data = models.JSONField(
        _('Исходные данные по которым был сформирован отчет'),
        null=True,
    )
    context = models.JSONField(
        _('Данные для формирования отчета'),
        null=True,
    )
    total_investment_amount_bi = models.FloatField(
        _('Общая сумма инвестирований из БД'),
        null=True,
    )
    total_investment_amount_math = models.FloatField(
        _('Общая сумма инвестирований, рассчитанная математически'),
        null=True,
    )
    sector = models.ForeignKey(
        'hincal.Sector',
        on_delete=models.CASCADE,
        verbose_name=_('Отрасль хозяйственной деятельности'),
        related_name='reports',
        null=True,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Отчет')
        verbose_name_plural = _('Отчеты')

    def __str__(self):
        return f'{self.user}: {self.created_at}'
