from typing import List, Tuple

import httpx
from django.conf import settings
from rest_framework import status

from server.apps.personal_cabinet.models import (
    Business,
    Sector,
    SubSector,
    TerritorialLocation,
)
from server.apps.personal_cabinet.services.enums import TypeBusiness
from server.apps.services.exception import ApiError
from server.apps.user.models import User

HANDLER_TERRITORIAL_LOCATION = {
    'восточный': 'wao',
    'западный': 'zao',
    'зеленоградский': 'zelao',
    'новомосковский': 'nao',
    'северный': 'sao',
    'северо-восточный': 'swao',
    'северо-западный': 'szao',
    'троицкий': 'tao',
    'центральный': 'cao',
    'южный': 'yuao',
    'юго-восточный': 'yuwao',
    'юго-западный': 'yuzao',
}


class ClientBase:
    """Базовый класс для API."""

    def __init__(self, base_url: str, token: str, secret: str = None):
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {token}",
        }
        if secret:
            headers["X-Secret"] = secret
        self._client = httpx.Client(base_url=base_url, headers=headers)

    def __aenter__(self) -> "ClientBase":
        return self

    def __aexit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """Close network connections"""
        self._client.close()

    def get(self, url, data, timeout=settings.DADATA_TIMEOUT_SEC):
        """GET request to Dadata API"""
        response = self._client.get(url, params=data, timeout=timeout)
        response.raise_for_status()
        return response.json()

    def post(self, url, data, timeout=settings.DADATA_TIMEOUT_SEC):
        """POST request to Dadata API"""
        response = self._client.post(url, json=data, timeout=timeout)
        response.raise_for_status()
        return response.json()


def get_business_by_inn(inn: str) -> List[dict]:
    """Получаем информацию о компании или ИП по inn из DaData."""
    # Проверяем настройки DaData
    if not (settings.DADATA_API_TOKEN and settings.DADATA_API_URL):
        raise ApiError(
            detail='Переменные для работы DaData не установлены.',
            code=status.HTTP_501_NOT_IMPLEMENTED,
        )
    # Создаем объект соединения с DaData и совершаем запрос с переданным inn.
    client = ClientBase(
        base_url=settings.DADATA_API_URL,
        token=settings.DADATA_API_TOKEN,
    )
    response = client.post(
        url=f'{settings.DADATA_API_URL}/findById/party',
        data={'query': inn},
    )

    return response.get('suggestions')


def create_or_update_business(inn: str, user_id: int) -> Tuple[Business, bool]:
    """Выбираем нужную информацию о компании или ИП и сохраняем ее в БД.

    Информация берется из DaData.
    """
    user = User.objects.get(id=user_id)
    business_information = get_business_by_inn(inn=inn)
    sector = Sector.objects.get(slug='other')
    sub_sector = SubSector.objects.get(slug='other')
    if business_information:
        business = business_information[0]
        data = business.get('data', {})
        address = data.get('address', {})
        territorial_location = TerritorialLocation.objects.get(
            slug=HANDLER_TERRITORIAL_LOCATION.get(
                address.get('data', {}).get('city_area', '').lower(),
            ),
        )
        return Business.objects.create_or_update(
            inn=inn,
            defaults={
                'type': data.get('type').lower(),
                'territorial_location':  territorial_location,
                'hid':  data.get('hid', ''),
                'short_business_name':  data.get('name', {}).get('short_with_opf', ''),
                'full_business_name':  data.get('name', {}).get('full_with_opf', ''),
                'management_name':  data.get('management', {}).get('name', ''),
                'management_position':  data.get('management', {}).get('post', ''),
                'full_opf':  data.get('opf', {}).get('full', ''),
                'short_opf':  data.get('opf', {}).get('short', ''),
                'okved':  data.get('okved', ''),
                'first_name':  data.get('fio', {}).get('name', ''),
                'last_name':  data.get('fio', {}).get('surname', ''),
                'middle_name':  data.get('fio', {}).get('patronymic', ''),
                'address':  address.get('unrestricted_value', ''),
                'country':  address.get('data', {}).get('country', ''),
                'region':  address.get('data', {}).get('region', ''),
                'city_area':  address.get('data', {}).get('city_area', ''),
                'city_district':  address.get('data', {}).get('city_district', ''),
                'phone':  data.get('phones', {})[0].get('value', ''),
                'email':  data.get('phones', {})[0].get('value', ''),
                'sector':  sector,
                'sub_sector':  sub_sector,
            },
        )
    else:
        return Business.objects.create_or_update(
            inn=inn,
            defaults={
                'type': TypeBusiness.PHYSICAL,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'middle_name': user.middle_name,
            },
        )
