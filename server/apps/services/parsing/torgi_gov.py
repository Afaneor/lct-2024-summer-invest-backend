import logging
import time

import requests

from server.apps.investment_object.models import Tender, TenderLot

logger = logging.getLogger('django')


def torgi_gov_parsing_tender():
    """Парсинг тендеров с сайта torgi.gov.ru."""
    # Формируем запрос к api для получения количества страниц.
    first_10_tender_json = requests.get(
        url=(
            'https://torgi.gov.ru/new/api/public/notices/search'
            '?subjRF=77,50'
            '&noticeStatus=PUBLISHED,APPLICATIONS_SUBMISSION'
            '&byFirstVersion=true'
            '&withFacets=true'
            '&size=10'
            '&sort=firstVersionPublicationDate,desc'
        ),
        timeout=15,
    ).json()
    total_pages = first_10_tender_json['totalPages']
    # Проходимся по всем страницам и получаем информацию.
    for number_page in range(total_pages):
        tenders_json = requests.get(
            url=(
                'https://torgi.gov.ru/new/api/public/notices/search'
                '?subjRF=77,50'
                '&noticeStatus=PUBLISHED,APPLICATIONS_SUBMISSION'
                '&byFirstVersion=true'
                f'&page={number_page}'
                f'&size=10'
                f'&sort=firstVersionPublicationDate,desc'
            ),
            timeout=15,
        ).json()
        for entity in tenders_json['content']:
            tender_id = entity['id']
            tender_url = (
                'https://torgi.gov.ru/new/api/public/notices/'
                f'noticeNumber/{tender_id}'
            )
            tender_json = requests.get(
                url=tender_url,
                timeout=15,
            ).json()

            tender, create = Tender.objects.get_or_create(
                tender_id=tender_id,
                bidding_type=tender_json.get('biddType', {}).get('name'),
                url=f'https://torgi.gov.ru/new/public/notices/view/{tender_id}',
            )

            for lot in tender_json.get('lots'):
                logger.info(
                    f"Найдено лотов: {len(tender_json.get('lots'))}. "
                    'Идет создание...',
                )

                extra_data = {
                    'Предмет торгов (наименование лота)': lot.get('lotName', ''),
                    'Описание лота': lot.get('lotDescription', ''),
                    'Вид торгов': lot.get('biddType', {}).get('name'),
                    'Категория объекта': lot.get('category', {}).get('name'),
                    'Начальная цена': lot.get('deposit', ''),
                    'Шаг аукциона': lot.get('priceStep', ''),
                    'Размер задатка': lot.get('priceMin', ''),
                    'Форма собственности':
                        lot.get('ownershipForm', {}).get('name'),
                    'Местонахождение имущества': lot.get('estateAddress', ''),
                    **{
                        data_json.get('name'): data_json.get('characteristicValue')
                        for data_json in lot.get('characteristics')
                        if data_json.get('name')
                    },
                }

                TenderLot.objects.get_or_create(
                    tender=tender,
                    tender_lot_id=lot['id'],
                    url=(
                        'https://torgi.gov.ru/new/public/lots/lot/'
                        f"{lot['id']}/(lotInfo:info)"
                    ),
                    name=lot.get('lotName'),
                    description=lot.get('lotDescription'),
                    extra_data=extra_data
                )

            logger.info(f"Обработано {entity['id']}")

            time.sleep(0.5)

        time.sleep(1)
        logger.info(f"Обработана {number_page}/{total_pages}")
