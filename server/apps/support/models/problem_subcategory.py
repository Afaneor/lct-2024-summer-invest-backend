from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class ProblemSubcategory(AbstractBaseModel):
    """Подкатегория проблемы."""

    problem_category = models.ForeignKey(
        to='support.ProblemCategory',
        on_delete=models.CASCADE,
        verbose_name=_('Категория проблемы'),
        related_name='problem_subcategories',
    )
    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Подкатегория проблемы')
        verbose_name_plural = _('Подкатегории проблем')

    def __str__(self):
        return self.name
