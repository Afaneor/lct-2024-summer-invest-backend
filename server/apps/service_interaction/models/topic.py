from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Topic(AbstractBaseModel):
    """Тема."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Тема')
        verbose_name_plural = _('Тема')
