from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class SelectedEntity(AbstractBaseModel):
    """Подобранные сущности для запроса на подбор."""

    investment_object = models.ForeignKey(
        to='investment_object.InvestmentObject',
        verbose_name=_('Инвестиционный объект'),
        on_delete=models.CASCADE,
        related_name='selected_entities',
        null=True,
    )
    service_support = models.ForeignKey(
        to='support.ServiceSupport',
        verbose_name=_('Сервис поддержки'),
        on_delete=models.CASCADE,
        related_name='selected_entities',
        null=True,
    )
    problem = models.ForeignKey(
        to='support.Problem',
        verbose_name=_('Проблема'),
        on_delete=models.CASCADE,
        related_name='selected_entities',
        null=True,
    )
    selection_request = models.ForeignKey(
        to='personal_cabinet.SelectionRequest',
        verbose_name=_('Запрос на подбор'),
        on_delete=models.CASCADE,
        related_name='selected_entities'
    )
    message = models.ForeignKey(
        to='personal_cabinet.Message',
        verbose_name=_(
            'Сообщение от бота, которое сформировало инвестиционные объекты',
        ),
        on_delete=models.CASCADE,
        related_name='selected_entities',
        blank=True,
        null=True,
    )
    is_relevant = models.BooleanField(
        verbose_name=_(
            'Соответствует ли объект пожеланию пользователя или нет',
        ),
        default=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Подобранная сущность для запроса')
        verbose_name_plural = _('Подобранные сущности для запроса')

    def __str__(self):
        return f'{self.selection_request} -> {self.investment_object}'
