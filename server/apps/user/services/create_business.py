from typing import List

import httpx
from django.conf import settings
from rest_framework import status

from server.apps.services.exception import ApiError

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
    """Base class for API client"""

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
