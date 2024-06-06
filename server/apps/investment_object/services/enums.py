from django.db import models
from django.utils.translation import gettext_lazy as _


class InfrastructureAvailability(models.TextChoices):
    """Наличие инфраструктуры"""

    POSSIBLE_CREATION = 'possible_creation', _('Возможно создание')
    YES = 'yes', _('Да')
    NOT_DATA = 'not_data', _('нет данных')
