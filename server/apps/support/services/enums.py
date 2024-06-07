from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeServiceSupport(models.TextChoices):
    """Тип сервиса."""

    SERVICE = 'service', _('Услуга')
    SUPPORT_MEASURE = 'support_measure', _('Мера поддержки')
