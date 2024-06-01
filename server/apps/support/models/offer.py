from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from server.apps.services.base_model import AbstractBaseModel


class Offer(AbstractBaseModel):
    """Партнерское предложение по инвестированию."""

    title = models.CharField(
        _('Заголовок'),
        max_length=settings.MAX_STRING_LENGTH,
    )
    text = models.TextField(
        _('Полное описание предложения'),
    )
    site = models.URLField(
        _('Ссылка на сторонний ресурс с подробной информацией'),
        blank=True,
    )
    interest_rate = models.CharField(
        _('Процентная ставка'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    loan_term = models.CharField(
        _('Срок займа'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    amount = models.CharField(
        _('Сумма займа'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    extra_data = models.JSONField(
        _('Дополнительные параметры'),
        null=True,
        blank=True,
    )
    tags = TaggableManager(blank=True)

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Партнерское предложение')
        verbose_name_plural = _('Партнерские предложения')

    def __str__(self):
        return self.title
