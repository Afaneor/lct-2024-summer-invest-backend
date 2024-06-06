from enum import Enum
from typing import Any


class ObjectType(Enum):
    """
    Типы объектов.
    """

    TECHNOPARK = 1
    TECHNOPOLIS = 2
    LAND = 3
    BUILDING = 4


def get_correct_data(row_data: Any, default: Any = ''):
    """Получение корректных значений."""
    return row_data if row_data else default


def clear_data(row_data: str):
    """Очистка данных от пробелов и лишних символов."""
    if row_data:
        row_data = row_data.strip()
        row_data = row_data.strip('\n')

    return row_data
