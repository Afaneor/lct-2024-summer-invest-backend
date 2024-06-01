from dataclasses import dataclass

from server.apps.hincal.services.enums import TypeBusiness


def get_cost_accounting():
    """Обертка для сохранения информации в поле модели."""
    return CostAccounting().data


def get_registration_costs():
    """Обертка для сохранения информации в поле модели."""
    return RegistrationCosts().data


def get_possible_income_from_patent():
    """Обертка для сохранения информации в поле модели."""
    return PossibleIncomeFromPatent().data


def get_possible_income_on_market():
    """Обертка для сохранения информации в поле модели."""
    return PossibleIncomeFromPatent().data


def get_average_salary_of_staff():
    """Обертка для сохранения информации в поле модели."""
    return AverageSalaryOfStaff().data


@dataclass
class AverageSalaryOfStaff:
    """Средняя заработная плата сотрудника, тыс. руб."""

    data = {
        'wao': 66.2442,
        'zao': 64.4345,
        'zelao': 50.4561,
        'nao': 48.5648,
        'sao': 63.8745,
        'swao': 57.7075,
        'szao': 56.2347,
        'tao': 46.3479,
        'cao': 82.2399,
        'yuao': 51.4685,
        'yuwao': 53.3458,
        'yuzao': 56.2499,
        'other': 61.9654,
    }


@dataclass
class PossibleIncomeFromPatent:
    """Возможные доходы по патентной системе по округам, тыс.руб."""

    data = {
        'wao': 6700,
        'zao': 5300,
        'zelao': 2600,
        'nao': 2800,
        'sao': 7600,
        'swao': 7400,
        'szao': 7400,
        'tao': 3500,
        'cao': 11400,
        'yuao': 5300,
        'yuwao': 5100,
        'yuzao': 5800,
        'other': 6000,
    }


@dataclass
class PossibleIncomeOnMarket:
    """Возможные рыночные доходы по округам, тыс.руб."""

    data = {
        'wao': 6700,
        'zao': 5300,
        'zelao': 2600,
        'nao': 2800,
        'sao': 7600,
        'swao': 7400,
        'szao': 7400,
        'tao': 3500,
        'cao': 11400,
        'yuao': 5300,
        'yuwao': 5100,
        'yuzao': 5800,
        'other': 6000,
    }


@dataclass
class CostAccounting:
    """Данные по ведению бухгалтерского учета, тыс. руб."""

    data = {
        'legal': {
            'osn': {
                'lower': 9,
                'upper': 40,
            },
            'ysn': {
                'lower': 7,
                'upper': 30,
            },
            'patent': {
                'lower': 0,
                'upper': 0,
            },
        },
        'individual': {
            'osn': {
                'lower': 6,
                'upper': 35,
            },
            'ysn': {
                'lower': 5,
                'upper': 25,
            },
            'patent': {
                'lower': 5,
                'upper': 25,
            },
        },
    }


@dataclass
class RegistrationCosts:
    """Расходы на регистрацию, тыс. руб."""

    data = {
        TypeBusiness.LEGAL: 40,
        TypeBusiness.INDIVIDUAL: 0.8,
    }
