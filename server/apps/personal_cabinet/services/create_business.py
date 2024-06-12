from typing import List, Optional, Tuple

import httpx
from django.conf import settings
from rest_framework import status

from server.apps.investment_object.models import EconomicActivity
from server.apps.personal_cabinet.models import (
    Business,
    TerritorialLocation,
)
from server.apps.services.exception import ApiError


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


def update_or_create_business(
    inn: str,
    user_id: int,
) -> Tuple[Optional[Business], bool]:
    """Выбираем нужную информацию о компании или ИП и сохраняем ее в БД.

    Информация берется из DaData.
    """
    business_information = get_business_by_inn(inn=inn)
    if business_information:
        business_suggestions = business_information[0]
        data = business_suggestions.get('data', {})
        address = data.get('address', {})
        territorial_location = TerritorialLocation.objects.get(
            full_name__icontains=address.get('data', {}).get('city_area', ''),
        )
        business, created = Business.objects.update_or_create(
            inn=inn,
            defaults={
                'user_id': user_id,
                'business_type': data.get('type').lower(),
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
                'phone': (
                    data.get('phones', [])[0].get('value', '')
                    if data.get('phones', [])
                    else
                    ''
                ),
                'email':  (
                    data.get('emails', [])[0].get('value', '')
                    if data.get('phones', [])
                    else
                    ''
                ),
            },
        )
        # Добавляем виды экономической деятельности.
        objects_for_add = []
        for economic_activity_row_data in data.get('okveds', ''):
            economic_activity, created = (
                EconomicActivity.objects.update_or_create(
                    code=economic_activity_row_data.get('code'),
                    name=economic_activity_row_data.get('name')
                )
            )
            objects_for_add.append(economic_activity)
        business.economic_activities.set(objects_for_add)

        return business, created

    return None, False
