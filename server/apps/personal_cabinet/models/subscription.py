from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.enums import SubscriptionType


class Subscription(AbstractBaseModel):
    """Подписка."""

    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='subscriptions',
        db_index=True,
    )
    subscription_type = models.CharField(
        verbose_name=_('Тип подписки'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=SubscriptionType.choices,
    )
    topics = models.ManyToManyField(
        to='service_interaction.Topic',
        verbose_name=_('Тема'),
        related_name='subscriptions',
        blank=True,
    )
    # Почему тут никнейм? Потому что за разными типами подписки могут
    # следить разные люди.
    telegram_username = models.CharField(
        verbose_name=_('Никнейм пользователя в телеграмме'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Подписка')
        verbose_name_plural = _('Подписки')
        constraints = [
            models.UniqueConstraint(
                name='unique_subscription_type_for_user',
                fields=('subscription_type', 'user')
            ),
        ]

    def __str__(self):
        return str(self.user)
