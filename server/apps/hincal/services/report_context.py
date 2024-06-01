import datetime
from dataclasses import dataclass
from typing import Union

from server.apps.hincal.models import Archive, Business
from server.apps.hincal.services.enums import TextForReport, TypeTaxSystem
from server.apps.hincal.services.offers_and_wishes_for_report import (
    add_offers_and_wishes_in_context,
)


def get_correct_data(entity, property_name):
    """Получение корректного значения."""
    if value := getattr(entity, property_name, None):
        return value
    return 'Данные не предоставлены'


def correct_float(value) -> Union[float, str]:
    """Корректно предоставляем информацию по расчетам в отчет."""
    if isinstance(value, float) and value and value > 0:
        return float('{:.3f}'.format(value))

    if isinstance(value, str) and value:
        return value

    return 'Нет данных'


@dataclass()
class ReportContextDataClass:
    """Дата класс контекста отчета."""

    # Дата формирования отчета.
    create_date: str = str(datetime.datetime.now())
    # Информация о бизнесе.
    business: Business = None
    # Исходные данные, которые ввел пользователь в калькуляторе.
    initial_data: dict = None
    # Информация о налогах, ставках и т.д.
    archive: Archive = None

    # Средние показатели расходов по другим бизнесам, которые есть в БД.
    avg_number_of_staff_bi: float = 0
    avg_salary_of_staff_bi: float = 0
    avg_taxes_to_the_budget_bi: float = 0
    avg_income_tax_bi: float = 0
    avg_property_tax_bi: float = 0
    avg_land_tax_bi: float = 0
    avg_personal_income_tax_bi: float = 0
    avg_transport_tax_bi: float = 0
    avg_other_taxes_bi: float = 0

    # Рассчитанные показатели расходов на основе математики.
    # Расходы по персоналу.
    avg_number_of_staff_math: float = 0
    avg_salary_of_staff_math: float = 0
    all_salary: float = 0
    avg_personal_income_tax_math: float = 0

    # Расходы по земле.
    avg_land_area_math: float = 0
    avg_land_cadastral_value_math: float = 0
    avg_land_tax_math: float = 0

    # Расходы по имуществу.
    property_area_math: float = 0
    avg_property_cadastral_value_math: float = 0
    avg_property_tax_math: float = 0
    avg_capital_construction_costs_math: float = 0
    type_capital_construction: str = ''

    # Средний размер налога на патент.
    avg_patent_tax_math: float = 0
    # Возможный доход предприятия по сектору.
    avg_possible_income_math: float = 0

    # Расходы на оборудование.
    equipment_costs: float = 0
    # Строковые представление данных об оборудовании.
    data_by_equipments_costs: str = ''
    # Расходы на бухгалтерские услуги.
    accounting_costs: float = 0
    # Расходы на регистрацию.
    registration_costs: float = 0
    # Прочие расходы
    others_costs: float = 0
    others_costs_str: str = ''
    # Тип налоговой системы.
    type_tax_system: str = ''

    def __post_init__(self):  # noqa: WPS231
        """Рассчитываем недостающие показатели."""
        # СТРАНИЦА 4.
        # Отчисления в ПФР согласно данным из БД.
        self.avg_staff_pension_contributions_costs_bi = (
            self.avg_number_of_staff_bi *
            self.avg_salary_of_staff_bi *
            self.archive.pension_contributions_rate
        )
        # Отчисления в ФМС согласно данным из БД.
        self.avg_staff_medical_contributions_costs_bi = (
            self.avg_number_of_staff_bi *
            self.avg_salary_of_staff_bi *
            self.archive.medical_contributions_rate
        )
        # Отчисления по нетрудоспособности согласно данным из БД.
        self.avg_staff_disability_contributions_costs_bi = (
            self.avg_number_of_staff_bi *
            self.avg_salary_of_staff_bi *
            self.archive.disability_contributions_rate
        )

        # Все расходы: з.п. сотрудников + НДФЛ +страховые взносы +
        # налог на прибыль, землю, имущество, транспорт, другие налоги,
        # патентную систему, бухгалтерию, оборудование, регистрацию.
        self.all_possible_costs_bi = (
            self.avg_salary_of_staff_bi +
            self.avg_personal_income_tax_bi +
            self.avg_staff_pension_contributions_costs_bi +
            self.avg_staff_medical_contributions_costs_bi +
            self.avg_staff_disability_contributions_costs_bi +
            self.avg_income_tax_bi +
            self.avg_property_tax_bi +
            self.avg_land_tax_bi +
            self.avg_transport_tax_bi +
            self.avg_other_taxes_bi +
            self.equipment_costs +
            self.accounting_costs +
            self.registration_costs +
            self.others_costs
        )
        # Все расходы на сотрудника: з.п. сотрудников + НДФЛ + страховые взносы
        self.all_staff_costs_bi = (
            self.avg_salary_of_staff_bi +
            self.avg_personal_income_tax_bi +
            self.avg_staff_pension_contributions_costs_bi +
            self.avg_staff_medical_contributions_costs_bi +
            self.avg_staff_disability_contributions_costs_bi
        )
        # Все расходы на землю и имущество: налог на землю, налог на имущество,
        # налог на транспорт.
        self.all_lp_tax_costs_bi = (
            self.avg_property_tax_bi +
            self.avg_land_tax_bi +
            self.avg_transport_tax_bi
        )
        # Все расходы на налоги.
        self.all_tax_costs_bi = (
            self.avg_personal_income_tax_bi +
            self.avg_income_tax_bi +
            self.avg_property_tax_bi +
            self.avg_land_tax_bi +
            self.avg_transport_tax_bi +
            self.avg_other_taxes_bi
        )
        # Все расходы на сервисы.
        self.all_services_costs_bi = (
            self.accounting_costs +
            self.registration_costs +
            self.others_costs
        )

        # ОБЩИЕ РАСХОДЫ СОГЛАСНО МАТЕМАТИКЕ.
        # Отчисления в ПФР согласно расчетам.
        self.avg_staff_pension_contributions_costs_math = (
            self.avg_number_of_staff_math *
            self.avg_salary_of_staff_math *
            self.archive.pension_contributions_rate
        )
        # Отчисления в ФМС согласно расчетам.
        self.avg_staff_medical_contributions_costs_math = (
            self.avg_number_of_staff_math *
            self.avg_salary_of_staff_math *
            self.archive.medical_contributions_rate
        )
        # Отчисления по нетрудоспособности согласно данным из БД.
        self.avg_staff_disability_contributions_costs_math = (
            self.avg_number_of_staff_math *
            self.avg_salary_of_staff_math *
            self.archive.disability_contributions_rate
        )

        # Расчет налога на прибыль.
        if self.avg_patent_tax_math:
            self.avg_income_tax_math = self.avg_patent_tax_math
        elif self.business and self.business.type_tax_system == TypeTaxSystem.OSN:  # noqa: E501
            self.avg_income_tax_math = (
                self.avg_possible_income_math *
                self.archive.osn_tax_rate
            )
        elif self.business and self.business.type_tax_system == TypeTaxSystem.YSN:  # noqa: E501
            self.avg_income_tax_math = (
                self.avg_possible_income_math *
                self.archive.ysn_tax_rate
            )
        else:
            self.avg_income_tax_math = (
                self.avg_possible_income_math *
                self.archive.osn_tax_rate
            )

        if self.type_tax_system == TypeTaxSystem.PATENT:
            self.all_possible_costs_math = (
                self.avg_salary_of_staff_math +
                self.avg_personal_income_tax_math +
                self.avg_staff_pension_contributions_costs_math +
                self.avg_staff_medical_contributions_costs_math +
                self.avg_staff_disability_contributions_costs_math +
                self.avg_income_tax_math +
                self.avg_land_tax_math +
                self.equipment_costs +
                self.accounting_costs +
                self.registration_costs +
                self.others_costs
            )
            # Расходы на землю.
            self.all_lp_tax_costs_math = self.avg_land_tax_math
            # Все расходы на налоги.
            self.all_tax_costs_math = (
                self.avg_personal_income_tax_math +
                self.avg_income_tax_math +
                self.avg_land_tax_math
            )
        else:
            self.all_possible_costs_math = (
                self.avg_salary_of_staff_math +
                self.avg_personal_income_tax_math +
                self.avg_staff_pension_contributions_costs_math +
                self.avg_staff_medical_contributions_costs_math +
                self.avg_staff_disability_contributions_costs_math +
                self.avg_income_tax_math +
                self.avg_property_tax_math +
                self.avg_land_tax_math +
                self.equipment_costs +
                self.accounting_costs +
                self.registration_costs +
                self.others_costs
            )

            # Все расходы на землю и имущество: налог на землю,
            # налог на имущество.
            self.all_lp_tax_costs_math = (
                self.avg_property_tax_math +
                self.avg_land_tax_math
            )
            # Все расходы на налоги.
            self.all_tax_costs_math = (
                self.avg_personal_income_tax_math +
                self.avg_income_tax_math +
                self.avg_property_tax_math +
                self.avg_land_tax_math
            )

        # Все расходы на сотрудника: з.п. сотрудников + НДФЛ + страховые взносы
        self.all_staff_costs_math = (
            self.avg_salary_of_staff_math +
            self.avg_personal_income_tax_math +
            self.avg_staff_pension_contributions_costs_math +
            self.avg_staff_medical_contributions_costs_math +
            self.avg_staff_disability_contributions_costs_math
        )

        # Все расходы на сервисы.
        self.all_services_costs_math = (
            self.accounting_costs +
            self.registration_costs +
            self.others_costs
        )

        # СТРАНИЦА 5.
        # Стоимость покупки/аренды имущества.
        avg_property_lease_costs = 0.0
        avg_property_purchase_costs = 0.0
        # Стоимость покупки/аренды земли.
        avg_land_lease_costs = 0.0
        avg_land_purchase_costs = 0.0

        territorial_locations = self.initial_data.get('territorial_locations')
        if territorial_locations:
            len_territorial_locations = len(territorial_locations)
            for territorial_location in territorial_locations:
                avg_property_lease_costs += territorial_location.avg_property_lease_costs  # noqa: E501
                avg_property_purchase_costs += territorial_location.avg_property_purchase_costs  # noqa: E501
                avg_land_lease_costs += territorial_location.avg_land_lease_costs  # noqa: E501
                avg_land_purchase_costs += territorial_location.avg_land_purchase_costs  # noqa: E501
        else:
            len_territorial_locations = 1
            avg_property_lease_costs += self.archive.avg_property_lease_costs
            avg_property_purchase_costs += self.archive.avg_property_purchase_costs  # noqa: E501
            avg_land_lease_costs += self.archive.avg_land_lease_costs
            avg_land_purchase_costs += self.archive.avg_land_purchase_costs

        # Средняя стоимость аренды/покупки квадратного метра имущества.
        self.avg_property_lease_value = (
            avg_property_lease_costs / len_territorial_locations
        )
        self.avg_property_purchase_value = (
            avg_property_purchase_costs / len_territorial_locations
        )
        # Средняя стоимость аренды/покупки квадратного метра земли.
        self.avg_land_lease_value = (
            avg_land_lease_costs / len_territorial_locations
        )
        self.avg_land_purchase_value = (
            avg_land_purchase_costs / len_territorial_locations
        )

        # Общая стоимость аренды/покупки имущества на год.
        self.avg_property_lease_costs = (
            self.avg_property_lease_value * self.property_area_math * 12
        )
        self.avg_property_purchase_costs = (
            self.avg_property_purchase_value * self.property_area_math
        )
        # Средняя стоимость аренды/покупки земли.
        self.avg_land_lease_costs = (
            self.avg_land_lease_value * self.avg_land_area_math * 12
        )
        self.avg_land_purchase_costs = (
            self.avg_land_purchase_value * self.avg_land_area_math
        )

        if self.business:
            indicator = self.business.business_indicators.first()
        else:
            indicator = None

        self.context_for_file = {
            # ИНФОРМАЦИЯ О ВАШЕЙ ОРГАНИЗАЦИИ, ЕСЛИ ЗАПРОС СДЕЛАЛ АВТОРИЗОВАННЫЙ
            # ПОЛЬЗОВАТЕЛЬ, КОТОРЫЙ ИМЕЕТ КОМПАНИЮ
            # Название сектора.
            'sector':
                get_correct_data(self.business, 'sector'),
            # Правовая форма (ООО, ИП).
            'full_opf':
                get_correct_data(self.business, 'full_opf'),
            # Количество сотрудников.
            'number_of_staff':
                correct_float(
                    get_correct_data(indicator, 'average_number_of_staff')),
            # Расположение.
            'territorial_location':
                get_correct_data(self.business, 'territorial_location'),
            # Тип системы налогооблажения.
            'type_tax_system':
                get_correct_data(self.business, 'type_tax_system'),
            # Примерное количество земли. кв.м.
            'business_land_area':
                correct_float(get_correct_data(indicator, 'land_area')),
            'business_property_area':
                correct_float(get_correct_data(indicator, 'property_area')),

            # Стандартные слова. Для каждой страницы из отчета
            'page_1': TextForReport.PAGE_ONE,
            'page_2': TextForReport.PAGE_TWO,
            'page_3': TextForReport.PAGE_THREE,
            'page_4': TextForReport.PAGE_FOUR,
            'page_5': TextForReport.PAGE_FIVE,
            'page_6': TextForReport.PAGE_SIX,

            # ИТОГОВЫЕ ЗНАЧЕНИЯ ВОЗМОЖНЫХ ЗАТРАТ НА ОСНОВЕ БД. ДАННЫЕ ЗАТРАТЫ
            # РАСЧИТыВАЮТСЯ НА ОСНОВЕ ДАННЫХ ИЗ БД.
            # Все затраты.
            'all_possible_costs_bi':
                correct_float(self.all_possible_costs_bi),
            # Все затраты на персонал.
            'all_staff_costs_bi':
                correct_float(self.all_staff_costs_bi),
            # Все затраты на землю и имущество.
            'all_lp_tax_costs_bi':
                correct_float(self.all_lp_tax_costs_bi),
            # Все затраты на оборудование.
            'equipment_costs_bi':
                correct_float(self.equipment_costs),
            # Все затраты на налоги.
            'all_tax_costs_bi':
                correct_float(self.all_tax_costs_bi),
            # Все затраты на сервисы. Бух учет и т.д.
            'all_services_costs_bi':
                correct_float(self.all_services_costs_bi),

            # ИТОГОВЫЕ ЗНАЧЕНИЯ ВОЗМОЖНЫХ ЗАТРАТ НА ОСНОВЕ МАТЕМАТИКИ.
            # ПРСОТО СЛОЖЕНИЕ, ВЫЧИТАНИЕ, УМНОЖЕНИЕ
            # Все затраты.
            'all_possible_costs_math':
                correct_float(self.all_possible_costs_math),
            # Все затраты на персонал.
            'all_staff_costs_math':
                correct_float(self.all_staff_costs_math),
            # Все затраты на землю и имущество.
            'all_lp_tax_costs_math':
                correct_float(self.all_lp_tax_costs_math),
            # Все затраты на оборудование.
            'equipment_costs_math':
                correct_float(self.equipment_costs),
            # Все затраты на налоги.
            'all_tax_costs_math':
                correct_float(self.all_tax_costs_math),
            # Все затраты на сервисы. Бух учет и т.д.
            'all_services_costs_math':
                correct_float(self.all_services_costs_math),

            # 4 Страница. Анализ расходов на персонал.
            # ИТОГОВЫЕ ЗНАЧЕНИЯ ЗАТРАТ НА ПЕРСОНАЛ НА ОСНОВЕ БД.
            # Затраты на зп за год.
            'avg_salary_of_staff_bi':
                correct_float(self.avg_salary_of_staff_bi),
            # Затраты на НДФЛ.
            'avg_personal_income_tax_bi':
                correct_float(self.avg_personal_income_tax_bi),
            # Затраты на отчисления по ПФР.
            'avg_staff_pc_costs_bi':
                correct_float(self.avg_staff_pension_contributions_costs_bi),
            # Затраты на отчисления по ОМС.
            'avg_staff_mc_costs_bi':
                correct_float(self.avg_staff_medical_contributions_costs_bi),
            # Затраты на отчисления по нетрудоспособности.
            'avg_staff_dc_costs_bi':
                correct_float(self.avg_staff_disability_contributions_costs_bi),

            # ИТОГОВЫЕ ЗНАЧЕНИЯ ЗАТРАТ НА ПЕРСОНАЛ НА ОСНОВЕ МАТЕМАТИКИ.
            # Затраты на зп за год.
            'avg_salary_of_staff_math':
                correct_float(self.avg_salary_of_staff_math),
            # Затраты на НДФЛ.
            'avg_personal_income_tax_math':
                correct_float(self.avg_personal_income_tax_math),
            # Затраты на отчисления по ПФР.
            'avg_staff_pc_costs_math':
                correct_float(self.avg_staff_pension_contributions_costs_math),
            # Затраты на отчисления по ОМС.
            'avg_staff_mc_costs_math':
                correct_float(self.avg_staff_medical_contributions_costs_math),
            # Затраты на отчисления по нетрудоспособности.
            'avg_staff_dc_costs_math':
                correct_float(
                    self.avg_staff_disability_contributions_costs_math),

            # 5 Страница. Сравнение цен имущества в аренду и в покупку.
            # Диапазон площади.
            # Диапазон площади имущества кв.м.
            'property_area': correct_float(self.property_area_math),
            # Диапазон площади земли кв.м.
            'land_area': correct_float(self.avg_land_area_math),

            # Стоимость кв.м. аренды имущества.
            'avg_property_lease_value':
                correct_float(self.avg_property_lease_value),
            # Общая стоимость по аренде.
            'avg_property_lease_costs':
                correct_float(self.avg_property_lease_costs),
            # Общие расходы по аренде имущества.
            'all_property_lease_costs':
                correct_float(
                    self.avg_property_lease_value * self.property_area_math),
            # Стоимость кв.м. покупки.
            'avg_property_purchase_value':
                correct_float(self.avg_property_purchase_value),
            # Общая стоимость по покупке.
            'avg_property_purchase_costs':
                correct_float(self.avg_property_purchase_costs),
            # Налог на недвижимость.
            'avg_property_tax':
                correct_float(self.avg_property_tax_math)
                if self.type_tax_system != TypeTaxSystem.PATENT
                else 'Налог по данной системе налогооблажения не уплачивается',
            # Общие расходы по покупке имущества.
            'all_property_purchase_costs':
                correct_float(
                    (
                        self.avg_property_purchase_value *
                        self.property_area_math +
                        self.avg_property_tax_math
                    ),
                ),

            # Стоимость кв.м. аренды земли.
            'avg_land_lease_value':
                correct_float(self.avg_land_lease_value),
            # Общая стоимость по аренде.
            'avg_land_lease_costs':
                correct_float(self.avg_land_lease_costs),
            # Общие расходы по аренде земли.
            'all_land_lease_costs':
                correct_float(
                    self.avg_land_lease_value * self.avg_land_area_math),

            # Стоимость кв.м. покупки земли.
            'avg_land_purchase_value':
                correct_float(self.avg_land_purchase_value),
            # Общая стоимость по покупке.
            'avg_land_purchase_costs':
                correct_float(self.avg_land_purchase_costs),
            # Налог на землю.
            'avg_land_tax':
                correct_float(self.avg_land_tax_math),
            # Общие расходы по покупке земли.
            'all_land_purchase_costs':
                correct_float(
                    (
                        self.avg_land_purchase_value *
                        self.avg_land_area_math +
                        self.avg_land_tax_math
                    ),
                ),

            # 6 Страница. Возможные неучитываемые расходы.
            # Другие расходы.
            'others_costs':
                (
                    self.others_costs_str +
                    '\a' +
                    f'Общие расходы составили: {self.others_costs} тыс. руб.'
                ),
            # Информация по оборудованию.
            'equipments': self.data_by_equipments_costs,

            # 7 Страница. Предложения по бизнесу (исходя из сферы).
            'offers_and_wishes': '',

            'avg_other_taxes_bi':
                correct_float(self.avg_other_taxes_bi),
            'avg_other_taxes_math': 0.0,
            'avg_income_tax_math':
                correct_float(self.avg_income_tax_math),
            'avg_income_tax_bi':
                correct_float(self.avg_income_tax_bi),
        }
