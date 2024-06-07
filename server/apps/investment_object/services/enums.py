from django.db import models
from django.utils.translation import gettext_lazy as _


class InfrastructureAvailability(models.TextChoices):
    """Наличие инфраструктуры"""

    POSSIBLE_CREATION = 'possible_creation', _('Возможно создание')
    YES = 'yes', _('Да')
    NOT_DATA = 'not_data', _('Нет данных')


class ObjectType(models.IntegerChoices):
    """Наличие инфраструктуры"""

    TECHNOPARK = 1, _('Технопарк')
    TECHNOPOLIS = 2, _('Технополис')
    LAND = 3, _('Земля')
    BUILDING = 4, _('Промплощадка')
    INDUSTRIAL_SITE = 5, _('Участки для промышленности.')
    CDT = 6, _('КРТ')
    TENDER = 7, _('Тендер')
    READY_BUSINESS = 8, _('Реальный бизнес')
    NOT_DATA = 9, _('Нет данных')
