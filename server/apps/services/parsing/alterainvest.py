import logging
import re
import time

import requests
from bs4 import BeautifulSoup, Tag

from server.apps.investment_object.models import ReadyBusiness

logger = logging.getLogger('django')


def alterainvest_parsing_ready_business():
    """Парсинг готового бизнеса с сайта alterainvest.ru."""
    # Формируем запрос к api для получения количества страниц.
    all_business_response = requests.get(
        url=(
            'https://alterainvest.ru/msk/products/'
        ),
        timeout=15,
    )
    all_business_data = BeautifulSoup(all_business_response.text, 'html.parser')
    number_pages = re.sub(
        '[\n\t\r ]',
        '',
        all_business_data.find('ul', class_='al-pagination mb20').contents[29].text,
    )
    for page_number in range(73, int(number_pages)+1):
        logger.info(f'Анализ страницы {page_number}')
        business_page_response = requests.get(
            url=(
                f'https://alterainvest.ru/msk/products/page-{page_number}'
            ),
            timeout=15,
        )
        business_page_data = BeautifulSoup(
            business_page_response.text,
            'html.parser',
        )

        for base_business_data in business_page_data.find_all('div', class_='al-cart-min _average al-box-white'):
            business_detail_url = base_business_data.contents[1].attrs.get('href')
            business_response = requests.get(
                url=(
                    f'https://alterainvest.ru/{business_detail_url}'
                ),
                timeout=15,
            )
            business_data = BeautifulSoup(
                business_response.text,
                'html.parser',
            )

            extra_data = {
                re.sub('[\n\t\r ]', '', business_characteristics.contents[1].text):
                    re.sub('[\n\t\r ]', '', business_characteristics.contents[3].text)
                for business_characteristics in business_data.find_all('div', class_='col-4 mb16')
                if len(business_characteristics.contents) > 3
            }
            name = re.sub(
                '[\n\t\r ]',
                '',
                business_data.find('h1', class_='heading3 mb12').text,
            )
            if business_data.find('div', class_='al-textcreator'):
                description = re.sub(
                    '[\n\t\r ]',
                    '',
                    business_data.find('div', class_='al-textcreator').text,
                )
            else:
                description = ''

            ReadyBusiness.objects.get_or_create(
                external_id=int(name.split('#')[1]),
                defaults={
                    'name': re.sub(
                        '[\n\t\r ]',
                        '',
                        business_data.find('h1', class_='heading3 mb12').text,
                    ),
                    'description': description,
                    'extra_data': extra_data,
                },
            )
            logger.info(f'Запись с id {name.split("#")[1]} добавлена')

        time.sleep(1)
