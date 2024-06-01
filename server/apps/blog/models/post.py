from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class Post(AbstractBaseModel):
    """Запись в блоге."""

    preview_image = models.ImageField(
        _('Изображение'),
        upload_to='media',
        blank=True,
    )
    title = models.CharField(
        _('Заголовок'),
        max_length=settings.MAX_STRING_LENGTH
    )
    text = models.TextField(
        _('Полное описание новости'),
    )
    is_published = models.BooleanField(
        _('Пост доступен для просмотра'),
        default=False,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Запись в блоге')
        verbose_name_plural = _('Записи в блоге')

    def __str__(self):
        return self.title
