from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Post(AbstractBaseModel):
    """Пост."""

    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='feedbacks',
        db_index=True,
    )
    topic = models.ForeignKey(
        to='service_interaction.Topic',
        on_delete=models.CASCADE,
        verbose_name=_('Тема'),
        related_name='posts',
        db_index=True,
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        verbose_name=_('Родительский пост'),
        related_name='children',
        db_index=True,
        null=True,
    )
    text = models.TextField(
        verbose_name=_('Текст'),
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
