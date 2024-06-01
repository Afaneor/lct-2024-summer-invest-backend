import logging
from typing import Any, Dict

import requests

from server.apps.investment_site.models.investment_site import InvestmentSite
from server.apps.investment_site.services.parsing.investment_object_type import (
    parsing_industrial_site_4,
    parsing_industrial_site_5,
    parsing_investment_catalog_3,
    parsing_technopark_1,
    parsing_technopolis_2, parsing_krt_6,
)

FUNCTION_MAP: Dict[int, Any] = {
    1: parsing_technopark_1,
    2: parsing_technopolis_2,
    3: parsing_investment_catalog_3,
    4: parsing_industrial_site_4,
    5: parsing_industrial_site_5,
    6: parsing_krt_6,
}

logger = logger = logging.getLogger('django')


def parsing_investment_site():
    response = requests.post(
        url=(
            'https://api.investmoscow.ru/investmoscow/investment-map/'
            'v1/investmentPlatform/searchInvestmentObjects'
        ),
        headers={'Content-Type': 'application/json'},
        json={
            'PageNumber': 1,
            'PageSize': 500,
            'districts': [],
            'metros': [],
        },
        timeout=15,
    )
    for entity in response.json()['entities']:
        investment_site, created = InvestmentSite.objects.get_or_create(
            investment_site_id=entity.get('investmentPlatformId'),
            defaults={
                'main_photo_url': entity.get('previewImgUrl'),
                'name': entity.get('name'),
                'coordinates': entity.get('coords'),
                'investment_object_type': entity.get('type'),
            },
        )
        FUNCTION_MAP.get(entity.get('type'))(
            investment_site=investment_site,
        )
        logger.info(f"Обработано {entity.get('name')}")
