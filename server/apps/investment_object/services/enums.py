from django.db import models
from django.utils.translation import gettext_lazy as _


class InfrastructureAvailability(models.TextChoices):
    """Наличие инфраструктуры"""

    POSSIBLE_CREATION = 'possible_creation', _('Возможно создание')
    YES = 'yes', _('Да')
    NOT_DATA = 'not_data', _('Нет данных')


class ObjectType(models.TextChoices):
    """Наличие инфраструктуры"""

    TECHNOPARK = 'technopark', _('Технопарк')
    TECHNOPOLIS = 'technopolis', _('Технополис')
    LAND_PLOT = 'land_plot', _('Земельный участок')
    BUILDING = 'building', _('Помещение')
    CDT = 'cdt', _('КРТ')
    TENDER_LOT = 'tender_lot', _('Лот тендера')
    READY_BUSINESS = 'ready_business', _('Реальный бизнес')
    OTHER = 'other', _('Другое')
    NOT_DATA = 'not_data', _('Нет данных')
