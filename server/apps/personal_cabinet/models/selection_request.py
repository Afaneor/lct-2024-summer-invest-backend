from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class SelectionRequest(AbstractBaseModel):
    """Запрос на подбор."""

    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='selection_requests',
        db_index=True,
        null=True,
    )
    anonymous_user_id = models.CharField(
        verbose_name=_('ID анонимного пользователя. Приходит с front'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    is_actual = models.BooleanField(
        verbose_name=_('Актуальный ли запрос на подбор или нет'),
        default=True,
    )
    is_bot_response_waiting = models.BooleanField(
        verbose_name=_('Ожидает ли запрос ответ от бота или нет'),
        default=False,
    )
    investment_objects = models.ManyToManyField(
        to='investment_object.InvestmentObject',
        verbose_name=_('Инвестиционный объект'),
        through='personal_cabinet.SelectedInvestmentObject',
        related_name='selection_results',
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Запрос на подбор')
        verbose_name_plural = _('Запросы на подборы')
        constraints = [
            models.UniqueConstraint(
                name='unique_is_actual_for_selection_request',
                condition=models.Q(('is_actual', True)),
                fields=('is_actual',)
            ),
        ]

    def __str__(self):
        return (
            f'{self.user}. '
            f'Актуальность запроса на подбор объектов: {self.is_actual}'
        )
