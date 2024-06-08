import logging
import time

import requests

from server.apps.investment_object.models import InvestmentObject, TenderLot
from server.apps.investment_object.services.enums import ObjectType

logger = logging.getLogger('django')


def parsing_tender_lot():
    """Парсинг тендеров с сайта torgi.gov.ru."""
    # Формируем запрос к api для получения количества страниц.
    # https://torgi.gov.ru/new/public/lots/reg.
    first_10_tender_lots_json = requests.get(
        url=(
            'https://torgi.gov.ru/new/api/public/lotcards/search'
            '?dynSubjRF=78,53&lotStatus=PUBLISHED,APPLICATIONS_SUBMISSION'
            '&byFirstVersion=true'
            '&withFacets=true'
            '&size=10'
            '&sort=firstVersionPublicationDate,desc'
        ),
        timeout=15,
    ).json()
    total_pages = first_10_tender_lots_json['totalPages']

    # Проходимся по всем страницам и получаем информацию.
    for number_page in range(total_pages):
        tender_lots_json = requests.get(
            url=(
                'https://torgi.gov.ru/new/api/public/lotcards/search'
                '?dynSubjRF=78,53'
                '&lotStatus=PUBLISHED,APPLICATIONS_SUBMISSION'
                '&byFirstVersion=true'
                '&withFacets=false'
                f'&page={number_page}'
                '&size=10'
                '&sort=firstVersionPublicationDate,desc'
            ),
            timeout=15,
        ).json()
        # В рамках страницы получаем информацию о лоте.
        # Берем его id, чтобы получить детальную информацию.
        for entity in tender_lots_json['content']:
            # Получаем id и делаем запрос.
            tender_lot_id = entity['id']
            tender_lot_url = (
                f'https://torgi.gov.ru/new/api/public/lotcards/{tender_lot_id}'
            )
            tender_lot_json = requests.get(
                url=tender_lot_url,
                timeout=15,
            ).json()

            # Формируем дополнительную информацию.
            extra_data = {
                'Предмет торгов (наименование лота)': tender_lot_json.get('lotName', ''),
                'Описание лота': tender_lot_json.get('lotDescription', ''),
                'Вид торгов': tender_lot_json.get('biddType', {}).get('name'),
                'Категория объекта': tender_lot_json.get('category', {}).get('name'),
                'Начальная цена': tender_lot_json.get('deposit', ''),
                'Шаг аукциона': tender_lot_json.get('priceStep', ''),
                'Размер задатка': tender_lot_json.get('priceMin', ''),
                'Форма собственности':
                    tender_lot_json.get('ownershipForm', {}).get('name'),
                'Местонахождение имущества': tender_lot_json.get('estateAddress', ''),
                **{
                    data_json.get('name'): data_json.get('characteristicValue')
                    for data_json in tender_lot_json.get('characteristics')
                    if data_json.get('name')
                },
            }

            # Получаем фотографии
            main_photo_url = (
                tender_lot_json.get('lotImages')[0]
                if tender_lot_json.get('lotImages')
                else ''
            )
            photo_urls = [
                (
                    'https://torgi.gov.ru/new/file-store/v1/'
                    f'{photo}?disposition=inline&resize=600x600!'
                )
                for photo in tender_lot_json.get('lotImages')
            ]

            # Получаем тип.
            object_type = tender_lot_json.get('category', {}).get('name')
            if object_type.lower().find('земл') >= 0:
                object_type = ObjectType.LAND_PLOT
            elif object_type.lower().find('помещ') >= 0:
                object_type = ObjectType.BUILDING
            else:
                object_type = ObjectType.OTHER

            # Получаем корректное имя лота тендера.
            name = tender_lot_json.get('lotName')
            if len(name) > 150:
                name = name.split(',')[0]

            investment_object, io_created = InvestmentObject.objects.get_or_create(
                external_id=tender_lot_id,
                name=name,
                defaults={
                    'main_photo_url': (
                        'https://torgi.gov.ru/new/file-store/v1/'
                        f'{main_photo_url}?disposition=inline&resize=600x600!'
                    ),
                    'photo_urls': photo_urls,
                    'object_type': object_type,
                },
            )

            # Формирование лота.
            TenderLot.objects.get_or_create(
                investment_object=investment_object,
                bidding_type=tender_lot_json.get('biddType', {}).get('name'),
                tender_lot_id=tender_lot_id,
                url=(
                    'https://torgi.gov.ru/new/public/lots/lot/'
                    f'{tender_lot_id}/(lotInfo:info)?fromRec=false'
                ),
                description=tender_lot_json.get('lotDescription'),
                extra_data=extra_data
            )

            logger.info(f"Обработано {entity['id']}")

            time.sleep(0.5)

        time.sleep(1)
        logger.info(f"Обработана {number_page}/{total_pages}")
