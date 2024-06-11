import logging
import re
import time

import requests
from bs4 import BeautifulSoup

from server.apps.investment_object.models import (
    EconomicActivity,
    InvestmentObject,
    ReadyBusiness,
    TransactionForm,
)
from server.apps.services.enums import ObjectType, TransactionFormType
from server.apps.services.parsing.xlsx.base import get_correct_data

logger = logging.getLogger('django')


def ready_business():
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
    ).strip()
    # int(number_pages)+1
    for page_number in range(1, 10):
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
                    f'https://alterainvest.ru{business_detail_url}'
                ),
                timeout=15,
            )
            business_data = BeautifulSoup(
                business_response.text,
                'html.parser',
            )

            # Дополнительные данные.
            extra_data = {
                re.sub('[\n\t\r ]', '', business_characteristics.contents[1].text).strip():
                    re.sub('[\n\t\r ]', '', business_characteristics.contents[3].text).strip()
                for business_characteristics in business_data.find_all('div', class_='col-4 mb16')
                if len(business_characteristics.contents) > 3
            }

            # Название бизнеса.
            name = re.sub(
                '[\n\t\r ]',
                '',
                business_data.find('h1', class_='heading3 mb12').text,
            ).strip()

            # Описание бизнеса.
            if business_data.find('div', class_='al-textcreator'):
                description = re.sub(
                    '[\n\t\r ]',
                    '',
                    business_data.find('div', class_='al-textcreator').text,
                ).strip()
            else:
                description = ''

            # Главная фотография.
            main_photo_url = business_data.find_all(
                'img',
                class_='image-sqr',
            )[0].attrs.get('src')

            # Стоимость.
            if extra_data.get('Стоимость'):
                cost = extra_data.get('Стоимость').replace(' ', '')[:-1]
            else:
                cost = None

            transaction_form, tf_created = (
                TransactionForm.objects.get_or_create(
                    name='Продажа',
                    transaction_form_type=TransactionFormType.SALE,
                )
            )
            investment_object, io_created = InvestmentObject.objects.update_or_create(
                name=name.split('#')[0],
                defaults={
                    'main_photo_url':
                        f'https://alterainvest.ru{main_photo_url}',
                    'object_type': ObjectType.READY_BUSINESS,
                    'transaction_form': transaction_form,
                    'cost': cost,
                    'location': (
                        extra_data.get('Район')
                        if extra_data.get('Район') != 'По запросу'
                        else ''
                    ),
                    'url': f'https://alterainvest.ru{business_detail_url}',
                },
            )

            if extra_data.get('Сфера деятельности'):
                objects_for_add = []
                for economic_activity_row_data in extra_data.get('Сфера деятельности').split(','):
                    economic_activity, created = (
                        EconomicActivity.objects.update_or_create(
                            name=get_correct_data(economic_activity_row_data),
                        )
                    )
                    objects_for_add.append(economic_activity)
                investment_object.economic_activities.set(objects_for_add)

            ReadyBusiness.objects.update_or_create(
                investment_object=investment_object,
                defaults={
                    'external_id': name.split('#')[1],
                    'description': description,
                    'extra_data': extra_data,
                },
            )
            logger.info(f'Запись с id {name.split("#")[1]} добавлена')

        time.sleep(1)
