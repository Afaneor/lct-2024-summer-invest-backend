from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.content_type_id import get_content_type_id
from server.apps.services.enums import EventType


class Event(AbstractBaseModel):
    """Событие."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    event_datetime = models.DateTimeField(
        verbose_name=_('Время проведения события'),
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )
    event_type = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=EventType.choices,
    )
    content_type = models.ForeignKey(
        to=ContentType,
        verbose_name=_('Тип содержимого'),
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField(
        verbose_name=_('Id объекта'),
    )
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Событие')
        verbose_name_plural = _('События')
        constraints = [
            models.CheckConstraint(
                name='event_type_valid',
                check=models.Q(event_type__in=EventType.values),
            ),
        ]

    @property
    def content_type_id(self) -> int:
        """Content type id утечки."""
        return get_content_type_id(self)
