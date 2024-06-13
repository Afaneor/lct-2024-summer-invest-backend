from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.content_type_id import get_content_type_id


class Topic(AbstractBaseModel):
    """Тема."""

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    shot_description = models.TextField(
        verbose_name=_('Краткое описание'),
        blank=True,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Тема')
        verbose_name_plural = _('Темы')

    @property
    def content_type_id(self) -> int:
        """Content type id утечки."""
        return get_content_type_id(self)
