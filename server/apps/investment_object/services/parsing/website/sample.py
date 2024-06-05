import logging
import re
import time
from typing import Dict

import requests
from bs4 import BeautifulSoup, Tag
from rest_framework import status

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_attractions():
    """
    Анализ достопримечательностей города Волгоград.

    Проходимся по всем достопримечательностям и анализируем их.
    """
    attractions_url = []
    number_page = 1
    while number_page is not None:
        attractions_response = requests.get(
            url=f'https://welcomevolgograd.com/visit/?PAGEN_1={number_page}'
        )
        if attractions_response.status_code != status.HTTP_200_OK:
            number_page += 1
            logger.info(f'Пропускаем страницу {number_page}')
            continue

        attractions_data = BeautifulSoup(attractions_response.text, 'html.parser')
        attractions = attractions_data.find_all('a', attrs={'target': '_blank'})
        for attraction in attractions:
            # Формируем url до достопримечательности и проверяем, анализировалось ли оно.
            url = f"https://welcomevolgograd.com{attraction.attrs.get('href')}"
            if url in attractions_url:
                continue

            logger.info(f'Анализ {url}')
            attractions_url.append(url)
            attraction_response = requests.get(url=url)

            # Если ошибка, то просто пропускаем
            if attraction_response.status_code != status.HTTP_200_OK:
                logger.info(f'Пропускаем {url}')
                continue

            attraction_data = BeautifulSoup(attraction_response.text, 'html.parser')
            data = parser_attraction_data(attraction_data=attraction_data)

        if attractions_data.find_all('div', class_='load_more'):
            number_page += 1
        else:
            number_page = None

        time.sleep(2)



def get_contact(contact_data) -> Dict[str, str]:
    """Парсинг контактной информации."""
    for content in contact_data.contents:
        if isinstance(content, Tag):
            if src_data := content.attrs.get('src'):
                if src_data.find('category_sight.svg') >= 0:
                    return {'categories': re.sub('[\n\t\r]', '', contact_data.text.strip())}
                if src_data.find('geotag_black.svg') >= 0:
                    return {'address': re.sub('[\n\t\r]', '', contact_data.text.strip())}
                if src_data.find('geotag_black.svg') >= 0:
                    return {'address': re.sub('[\n\t\r]', '', contact_data.text.strip())}
                if src_data.find('call.svg') >= 0:
                    return {'phone': re.sub('[\n\t\r]', '', contact_data.text.strip())}
                if src_data.find('web.svg') >= 0:
                    return {'site': re.sub('[\n\t\r]', '', contact_data.text.strip())}
            # Для телефона и сайта необходимо провалиться на уровень ниже,
            # поэтому этот уровень вызывается рекурсией.
            if content.attrs.get('href'):
                return get_contact(contact_data=content)


def parser_attraction_data(attraction_data: BeautifulSoup):
    """
    Анализ конкрентной достопримечтальности.

    Получение имени, описнаия, фотографий, контактных данных.
    """
    name = re.sub('[\n\t\r ]', '', attraction_data.find('h1').text.strip())
    description = re.sub('[\n\t\r ]', '', attraction_data.find('div', class_='descBlock-description').text.strip())
    photos = [
        f"https://welcomevolgograd.com{photo.attrs.get('href')}"
        for photo in attraction_data.find_all('a', attrs={'data-fancybox': 'gallery'})
    ]

    contacts_data = {}
    for contact_data in attraction_data.find_all('div', class_='contact-item'):
        contacts_data.update(**get_contact(contact_data=contact_data))

    return name, description, photos, contacts_data


get_attractions()
