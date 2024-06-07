import logging

import requests

from server.apps.services.parsing.xlsx.base import clear_data
from server.apps.support.models import ServiceSupport
from server.apps.support.services.enums import TypeService

logger = logging.getLogger('django')


def parsing_service():
    """Парсинг сервисов investmoscow.ru"""
    # Получаем https://investmoscow.ru/catalog/search
    response = requests.post(
        url=(
            'https://api.investmoscow.ru/common/usoz-services/v1/'
            'services/searchPublished'
        ),
        headers={
            'Content-Type': 'application/json'
        },
        json={
            'PageNumber': 1,
            'PageSize': 500,
        },
        timeout=15,
    )
    for entity in response.json().get('entities'):
        entity_url = (
            'https://api.investmoscow.ru/common/usoz-services/v1/services/'
            f"getPublishedService/{entity.get('id')}"
        )
        entity_response = requests.get(url=entity_url).json()
        type_services = {
            'меры поддержки': TypeService.SUPPORT_MEASURE,
            'услуги': TypeService.SERVICE,
        }
        services = ServiceSupport.objects.filter(
            name=entity.get('name'),
        )
        if services.exists():
            service = services.first()
            service.type_service = entity.get('categoryName', '').lower()
            service.external_id = entity.get('id')
            service.url = entity_url
        else:
            service, created = ServiceSupport.objects.get_or_create(
                external_id=entity.get('id'),
                defaults={
                    'region': 'Москва',
                    'type_service':
                        clear_data(
                            row_data=type_services.get(
                                entity.get('serviceTypeName'),
                            ),
                        ),
                    'name':
                        clear_data(row_data=entity.get('name')),
                    'support_type':
                        clear_data(
                            row_data=entity.get('categoryName', '').lower(),
                        ),
                    'support_level': 'региональные меры',
                    'description':
                        clear_data(
                            row_data=entity_response.get(
                                'common',
                            ).get(
                                'fullDescription',
                            )
                        ),
                    'legal_act':
                        clear_data(
                            row_data=entity_response.get(
                                'reasons',
                            ).get(
                                'regulatoryLegalActs',
                            )[0].get(
                                'name'
                            )
                        ),
                    'url_legal_act':
                        clear_data(
                            row_data=entity_response.get(
                                'reasons',
                            ).get(
                                'regulatoryLegalActs',
                            )[0].get(
                                'link'
                            )
                        ),
                    'url': entity_url,
                }
            )


        logger.info(f'Обработана запись: {service.name}')
