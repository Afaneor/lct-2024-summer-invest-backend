from typing import Any, Dict, List

import requests

from server.apps.investment_object.models.investment_object import (
    InvestmentObject,
)

URL_MAPPING: Dict[int, str] = {
    # ТЕХНОПАРКИ. https://investmoscow.ru/business/technoparks
    1: 'https://api.investmoscow.ru/investmoscow/industry/v1/techpark/get?id={id}',
    # ПЛОЩАДКИ ОЭЗ "ТЕХНОПОЛИC".
    # https://investmoscow.ru/business/sez-technopolis-moscow
    2: 'https://api.investmoscow.ru/investmoscow/industry/v1/economiczone/getseztechnopolismoscowsite?id={id}',
    # ИНВЕСТИЦИОННЫЙ КАТАЛОГ. https://investmoscow.ru/business/invest-catalog
    3: 'https://api.investmoscow.ru/investmoscow/industry/v1/investcatalog/getobject?id={id}',
    # РЕЕСТР ПРОМПЛОЩАДОК. https://investmoscow.ru/business/site-list
    4: 'https://api.investmoscow.ru/investmoscow/industry/v1/industryzone/getroomforindustrial?id={id}',
    # РЕЕСТР ПРОМПЛОЩАДОК. ЗЕМЕЛЬНЫЕ УЧАСТКИ.
    # https://investmoscow.ru/business/site-list
    5: 'https://api.investmoscow.ru/investmoscow/industry/v1/industryzone/getsiteforindustrial?id={id}',
    # КРТ.
    # https://investmoscow.ru/business/krt
    6: 'https://api.investmoscow.ru/investmoscow/industry/v1/krt/getById?id={id}'
}


def parsing_technopark_1(
    investment_site: InvestmentObject,
):
    """Парсинг технопарков."""
    # Формируем запрос к api.
    url_for_parsing = URL_MAPPING.get(
        investment_site.inobject_type,
    ).format(
        id=investment_site.investment_site_id,
    )
    response_json = requests.get(
        url=url_for_parsing,
        headers={'Content-Type': 'application/json'},
        timeout=15,
    ).json()

    generic_info_tab = response_json.get('genericInfoTab')
    contact_info_tab = response_json.get(
        'contactInfoTab',
    )

    extra_data = {
        # Общая информация.
        'Наименование': generic_info_tab.get('name', ''),
        'Общая информация': generic_info_tab.get('generalInfo', ''),
        'Специализация': ', '.join(generic_info_tab.get('specializations', [])),
        # Контакты.
        'Адрес': contact_info_tab.get('address', ''),
        'Управляющая компания': contact_info_tab.get('managementCompany', ''),
        'Урл сайта': contact_info_tab.get('url', ''),
        'Контактное лицо': contact_info_tab.get('contactPerson', ''),
        'Телефон': contact_info_tab.get('phone', ''),
    }

    # Добавляем фотографии, если они есть
    investment_site.photo_urls = response_json.get('photoUrls')
    investment_site.extra_data = extra_data
    investment_site.url_from_site = (
        'https://investmoscow.ru/business/'
        f'technoparks/{investment_site.investment_site_id}'
    )
    investment_site.save(
        update_fields=['photo_urls', 'extra_data', 'detail_url'],
    )


def parsing_technopolis_2(
    investment_site: InvestmentObject,
):
    """Парсинг технополисов."""
    # Формируем запрос к api.
    url_for_parsing = URL_MAPPING.get(
        investment_site.inobject_type,
    ).format(
        id=investment_site.investment_site_id,
    )
    response_json = requests.get(
        url=url_for_parsing,
        headers={'Content-Type': 'application/json'},
        timeout=15,
    ).json()

    generic_info_tab = response_json.get('genericInfoTab')
    engineering_infrastructure_tab = response_json.get(
        'engineeringInfrastructureTab',
    )

    extra_data = {
        # Общая информация.
        'Наименование':
            generic_info_tab.get('name', ''),
        'Округ':
            generic_info_tab.get('okrug', ''),
        'Общая площадь, м2, га':
            generic_info_tab.get('area', ''),
        'Количество резидентов особой экономической зоны':
            generic_info_tab.get('residentsCount', ''),
        'Объем инвестиций, млрд руб':
            generic_info_tab.get('investmentSize', ''),
        'Количество рабочих мест':
            generic_info_tab.get('workplacesCount', ''),
        # инженерная инфраструктура.
        'Электроснабжение. Максимально допустимая мощность.':
            engineering_infrastructure_tab.get('powerSupplyMaxAvailablePower', ''),
        'Электроснабжение. Свободная мощность':
            engineering_infrastructure_tab.get('powerSupplyFreePower', ''),
        'Водоснабжение. Максимально допустимая мощность.':
            engineering_infrastructure_tab.get('waterSupplyMaxAvailablePower', ''),
        'Водоснабжение. Свободная мощность':
            engineering_infrastructure_tab.get('waterSupplyFreePower', ''),
        'Водоотведение. Максимально допустимая мощность.':
            engineering_infrastructure_tab.get('sewersMaxAvailablePower', ''),
        'Водоотведение. Свободная мощность':
            engineering_infrastructure_tab.get('sewersFreePower', ''),
        'Теплоснабжение. Максимально допустимая мощность.':
            engineering_infrastructure_tab.get('heatingSupplyMaxAvailablePower', ''),
        'Теплоснабжение. Свободная мощность':
            engineering_infrastructure_tab.get('heatingSupplyFreePower', ''),
    }

    # Добавляем фотографии, если они есть
    investment_site.photo_urls = response_json.get('photoUrls')
    investment_site.extra_data = extra_data
    investment_site.detail_url = (
        'https://investmoscow.ru/business/'
        f'sez-technopolis-moscow/{investment_site.investment_site_id}'
    )
    investment_site.save(
        update_fields=['photo_urls', 'extra_data', 'detail_url'],
    )


def parsing_investment_catalog_3(
    investment_site: InvestmentObject,
):
    """Парсинг технопарков."""
    # Формируем запрос к api.
    url_for_parsing = URL_MAPPING.get(
        investment_site.inobject_type,
    ).format(
        id=investment_site.investment_site_id,
    )
    response_json = requests.get(
        url=url_for_parsing,
        headers={'Content-Type': 'application/json'},
        timeout=15,
    ).json()

    building_tab = response_json.get('buildingTab')
    land_plot_tab = response_json.get('landPlotTab')

    extra_data = {
        # Здание.
        'Количество объектов': building_tab.get('count', '0'),
        'Год постройки': building_tab.get('year', ''),
        'Площадь постройки': building_tab.get('area', '0'),
        # Земельный участок.
        'Площадь': land_plot_tab.get('area', ''),
        'Единица изменения площади': land_plot_tab.get('areaUnit', ''),
        'Кадастровый № ЗУ': land_plot_tab.get('cadastralNumber', ''),
        'Дата ГПЗУ': land_plot_tab.get('gpzuDate', ''),
        'Номер ГПЗУ': land_plot_tab.get('gpzuNumber', ''),
        'ВРИ': land_plot_tab.get('vri', ''),

    }

    investment_site.photo_urls = response_json.get('photoUrls')
    investment_site.extra_data = extra_data
    investment_site.detail_url = (
        'https://investmoscow.ru/business/'
        f'invest-catalog/{investment_site.investment_site_id}'
    )
    investment_site.save(
        update_fields=['photo_urls', 'extra_data', 'detail_url'],
    )


def parsing_industrial_site_4(
    investment_site: InvestmentObject,
):
    """Парсинг промплощадок."""
    # Формируем запрос к api.
    url_for_parsing = URL_MAPPING.get(
        investment_site.inobject_type,
    ).format(
        id=investment_site.investment_site_id,
    )
    response_json = requests.get(
        url=url_for_parsing,
        headers={'Content-Type': 'application/json'},
        timeout=15,
    ).json()

    generic_info_tab = response_json.get('genericInfoTab')
    room_for_rent_tab = response_json.get(
        'roomForRentTab',
    )

    extra_data = {
        # Здание.
        'Наименование': generic_info_tab.get('name', ''),
        'Вид объекта': generic_info_tab.get('kind', ''),
        'Адрес': generic_info_tab.get('address', ''),
        'Округ': generic_info_tab.get('okrug', ''),
        'Основная информация': generic_info_tab.get('desc', ''),
        'Площадь земельного участка': generic_info_tab.get('groundArea', ''),
        # Помещения под аренду.
        'Парковка': room_for_rent_tab.get('parking', ''),
        'Вода': room_for_rent_tab.get('water', ''),
        'Отопление': room_for_rent_tab.get('heating', ''),
        'Электроэнергия': room_for_rent_tab.get('electricity', ''),
        'Площадь помещений под аренду': room_for_rent_tab.get('area', ''),
        'Стоимость площадки': room_for_rent_tab.get('price', ''),
        'Тип площадки': room_for_rent_tab.get('type', ''),
    }

    investment_site.photo_urls = response_json.get('photoUrls')
    investment_site.extra_data = extra_data
    investment_site.detail_url = (
        'https://investmoscow.ru/business/site-details/'
        f'room/{investment_site.investment_site_id}'
    )
    investment_site.save(
        update_fields=['photo_urls', 'extra_data', 'detail_url'],
    )


def parsing_industrial_site_5(
    investment_site: InvestmentObject,
):
    """Парсинг промплощадок (земельных участков)."""
    # Формируем запрос к api.
    url_for_parsing = URL_MAPPING.get(
        investment_site.inobject_type,
    ).format(
        id=investment_site.investment_site_id,
    )
    response_json = requests.get(
        url=url_for_parsing,
        headers={'Content-Type': 'application/json'},
        timeout=15,
    ).json()

    generic_info_tab = response_json.get('genericInfoTab')
    technical_and_economic_indicators_tab = response_json.get(
        'technicalAndEconomicIndicatorsTab',
    )

    extra_data = {
        # Общая информация.
        'Наименование': generic_info_tab.get('name', ''),
        'Вид объекта': generic_info_tab.get('kind', ''),
        'Адрес': generic_info_tab.get('address', ''),
        'Округ': generic_info_tab.get('okrug', ''),
        'Кадастровый номер земельного участка': generic_info_tab.get('cadastrNumber', ''),
        'Основная информация': generic_info_tab.get('desc', ''),
        'Площадь земельного участка': generic_info_tab.get('groundArea', ''),
        'Назначение земельного участка': generic_info_tab.get('landPurpose', ''),
        'Требуется внести изменения ПЗЗ г. Москвы': generic_info_tab.get('needToMakeChangesToPzzOfMoscow', False),
        # Технико-экономические показатели.
        'Максимальный процент застройки': technical_and_economic_indicators_tab.get('maxBuildingPercent', ''),
        'Плотность застройки': technical_and_economic_indicators_tab.get('maxDensity', ''),
        'Высотность': technical_and_economic_indicators_tab.get('maxHeight', ''),
    }

    investment_site.photo_urls = response_json.get('photoUrls')
    investment_site.extra_data = extra_data
    investment_site.detail_url = (
        'https://investmoscow.ru/business/site-details/'
        f'room/{investment_site.investment_site_id}'
    )
    investment_site.save(
        update_fields=['photo_urls', 'extra_data', 'detail_url'],
    )


def parsing_krt_6(
    investment_site: InvestmentObject,
):
    """Парсинг КРТ."""
    # Формируем запрос к api.
    url_for_parsing = URL_MAPPING.get(
        investment_site.inobject_type,
    ).format(
        id=investment_site.investment_site_id,
    )
    response_json = requests.get(
        url=url_for_parsing,
        headers={'Content-Type': 'application/json'},
        timeout=15,
    ).json()

    extra_data = {
        # Земельный участок.
        'Кадастровый номер': response_json.get('cadastralNumber', ''),
        'Площадь': response_json.get('area', ''),
        'Округ': response_json.get('okrug', ''),
        'Статус проекта': response_json.get('status', ''),
        'Адрес': response_json.get('address', ''),
        # Технико-экономические показатели.
        'Площадь застройки производственного назначения': response_json.get('areaProduction', ''),
        'Площадь застройки общественно-делового назначения': response_json.get('areaPublicAndBusiness', ''),
        'Суммарная поэтажная площадь застройки в ГНС': response_json.get('areaSumGNS', ''),
        'Площадь существующей застройки': response_json.get('areaExistingConstruction', ''),
        'Количество правообладателей': response_json.get('numberOwners', ''),
        'Количество рабочих мест': response_json.get('numberWorkplaces', ''),
        'Выкуп ЗИК': response_json.get('buybackZIK', ''),
        'Виды разрешенного использования': get_correct_data_from_dict(
            key_name='name',
            all_data_json=response_json.get('vriZu', []),
        ),

    }

    investment_site.photo_urls = response_json.get('photoUrls')
    investment_site.extra_data = extra_data
    investment_site.detail_url = (
        'https://investmoscow.ru/business/'
        f'krt/{investment_site.investment_site_id}'
    )
    investment_site.save(
        update_fields=['photo_urls', 'extra_data', 'detail_url'],
    )


def get_correct_data_from_dict(
    key_name: str,
    all_data_json: List[Dict[str, Any]],
) -> str:
    """Формирование корректной строки из словаря."""
    str_data = ''
    for data_json in all_data_json:
        str_data += data_json.get(key_name, '') + '; '

    return str_data[:-1]
