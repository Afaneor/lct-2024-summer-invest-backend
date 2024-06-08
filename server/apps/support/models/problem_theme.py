from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class ProblemTheme(AbstractBaseModel):
    """Тема проблемы."""

    problem_subcategory = models.ForeignKey(
        to='support.ProblemSubcategory',
        on_delete=models.CASCADE,
        verbose_name=_('Подкатегория проблемы'),
        related_name='problem_themes',
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
        verbose_name = _('Тема проблемы')
        verbose_name_plural = _('Темы проблем')

    def __str__(self):
        return self.name
