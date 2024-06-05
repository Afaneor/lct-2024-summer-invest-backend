from enum import Enum

from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeBusiness(models.TextChoices):
    """Тип бизнеса: ИП, физическое лицо или компания."""

    LEGAL = 'legal', _('Юридическое лицо')
    INDIVIDUAL = 'individual', _('Индивидуальный предприниматель')
    PHYSICAL = 'physical', _('Физическое лицо')


class TypeBusinessForCalculator(models.TextChoices):
    """Тип бизнеса: ИП, физическое лицо или компания."""

    LEGAL = 'legal', _('Юридическое лицо')
    INDIVIDUAL = 'individual', _('Индивидуальный предприниматель')


class TypeTaxSystem(models.TextChoices):
    """Тип системы налогооблажения."""

    OSN = 'osn', _('Общая')
    YSN = 'ysn', _('Упрощенная')
    PATENT = 'patent', _('Патентная')


class PropertyType(models.TextChoices):
    """Типы зданий."""

    WORKSHOP_BUILDING = 'workshop_building', _('Здание цеха')
    WAREHOUSE_SPACE = 'warehouse_space', _('Складское помещение')
    ADMINISTRATIVE_BUILDING = 'administrative_building', _('Административное здание')  # noqa: E501
    OTHER = 'other', _('Другие типы')


class MessageOwnerType(models.TextChoices):
    """Владелец сообщения"""

    USER = 'user', _('Пользователь')
    BOT = 'bot', _('Бот')
