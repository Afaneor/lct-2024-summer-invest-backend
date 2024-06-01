from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class Support(AbstractBaseModel):
    """Меры поддержки бизнеса."""

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
        _('Полное описание меры'),
    )
    amount = models.CharField(
        _('Сумма субсидий'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    site = models.URLField(
        _('Ссылка на сторонний ресурс с подробной информацией'),
        blank=True,
    )
    extra_data = models.JSONField(
        _('Дополнительные параметры'),
        null=True,
        blank=True,
    )
    is_actual = models.BooleanField(
        _('Является ли меря поддержки актуальной'),
        default=False,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Мера поддержки бизнеса')
        verbose_name_plural = _('Меры поддержки бизнеса')

    def __str__(self):
        return self.title
