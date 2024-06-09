from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.enums import MessageOwnerType
from server.apps.services.base_model import AbstractBaseModel


class Message(AbstractBaseModel):
    """Сообщение."""

    owner_type = models.CharField(
        verbose_name=_('Владелец'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=MessageOwnerType.choices,
        default=MessageOwnerType.USER
    )
    selection_request = models.ForeignKey(
        to='personal_cabinet.SelectionRequest',
        verbose_name=_('Запрос на подбор'),
        on_delete=models.CASCADE,
        related_name='messages'
    )
    text = models.TextField(
        verbose_name=_('Текст'),
    )
    filter = models.JSONField(
        verbose_name=_('Фильтры для инвестиционных объектов'),
        blank=True,
        null=True,
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        verbose_name=_('Родительское сообщение'),
        related_name='children',
        db_index=True,
        null=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')
        constraints = [
            models.CheckConstraint(
                name='owner_type_valid',
                check=models.Q(owner_type__in=MessageOwnerType.values),
            ),
        ]

    def __str__(self):
        return self.owner_type
