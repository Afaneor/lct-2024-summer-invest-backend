from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.content_type_id import get_content_type_id


class Problem(AbstractBaseModel):
    """Проблема."""

    problem_theme = models.ForeignKey(
        to='support.ProblemTheme',
        on_delete=models.CASCADE,
        verbose_name=_('Тема проблемы'),
        related_name='problems',
    )
    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        unique=True,
    )
    name = models.TextField(
        verbose_name=_('Название проблемы'),
    )
    additional_info = models.TextField(
        verbose_name=_('Дополнительная информация'),
        blank=True,
    )
    url = models.CharField(
        verbose_name=_('Ссылка на объект'),
        max_length=settings.MAX_STRING_LENGTH,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Проблема')
        verbose_name_plural = _('Проблемы')

    def __str__(self):
        return self.name

    @property
    def content_type_id(self) -> int:
        """Content type id утечки."""
        return get_content_type_id(self)
