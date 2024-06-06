import logging
from typing import Any, Dict

import requests

from server.apps.investment_object.models.investment_object import (
    InvestmentObject,
)
from server.apps.investment_object.services.parsing.website.investment_object_type import (
    parsing_industrial_site_4,
    parsing_industrial_site_5,
    parsing_investment_catalog_3,
    parsing_krt_6,
    parsing_technopark_1,
    parsing_technopolis_2,
)

FUNCTION_MAP: Dict[int, Any] = {
    1: parsing_technopark_1,
    2: parsing_technopolis_2,
    3: parsing_investment_catalog_3,
    4: parsing_industrial_site_4,
    5: parsing_industrial_site_5,
    6: parsing_krt_6,
}

logger = logging.getLogger('django')


def parsing_investmoscow():
    """Парсинг данных с сайта investmoscow.ru"""
    # Получаем https://investmoscow.ru/about-moscow/investment-map-v2
    response = requests.post(
        url=(
            'https://api.investmoscow.ru/investmoscow/investment-map/'
            'v1/investmentPlatform/searchInvestmentObjects'
        ),
        headers={
            'Content-Type': 'application/json'
        },
        json={
            'PageNumber': 1,
            'PageSize': 500,
            'districts': [],
            'metros': [],
        },
        timeout=15,
    )
    for entity in response.json()['entities']:
        if entity.get('coords'):
            if entity.get('coords').get('type') == 'Point':
                longitude = entity.get('coords').get('coordinates')[0]
                latitude = entity.get('coords').get('coordinates')[1]
            elif entity.get('coords').get('type') == 'Polygon':
                longitude = entity.get('coords').get('coordinates')[0][0][0]
                latitude = entity.get('coords').get('coordinates')[0][0][1]
            elif entity.get('coords').get('type') == 'MultiPolygon':
                longitude = entity.get('coords').get('coordinates')[0][0][0][0]
                latitude = entity.get('coords').get('coordinates')[0][0][0][1]
            else:
                longitude = None
                latitude = None
        else:
            longitude = None
            latitude = None

        investment_site, created = InvestmentObject.objects.get_or_create(
            external_id=entity.get('investmentPlatformId'),
            defaults={
                'main_photo_url': entity.get('previewImgUrl'),
                'name': entity.get('name'),
                'longitude': longitude,
                'latitude': latitude,
                'object_type': entity.get('type'),
            },
        )
        FUNCTION_MAP.get(entity.get('type'))(
            investment_site=investment_site,
        )
        logger.info(f"Обработано {entity.get('name')}")
