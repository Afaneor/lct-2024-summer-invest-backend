from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Comment(AbstractBaseModel):
    """Комментарий."""

    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='comments',
        db_index=True,
    )
    text = models.TextField(
        verbose_name=_('Текст'),
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
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
