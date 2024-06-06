import logging

import requests

from server.apps.support.models import ProblemReport

logger = logging.getLogger('django')


def parsing_problem():
    """Парсинг данных о проблемах с сайта investmoscow.ru"""
    # Получаем https://investmoscow.ru/business/moscow-investor
    response = requests.get(
        url=(
            'https://services.investmoscow.ru/moscowinvestorapi/'
            'appealcategories/list/v2'
        ),
        timeout=15,
    )
    for category in response.json():
        for subcategory in category.get('subcategories', []):
            for theme in subcategory.get('themes', []):
                for problem in theme.get('problems', []):
                    external_id = problem.get('id')
                    problem, created = ProblemReport.objects.get_or_create(
                        external_id=problem.get('id'),
                        defaults={
                            'name': problem.get('name'),
                            'additional_info': problem.get('faq'),
                            'external_theme_id': theme.get('id'),
                            'theme_name': theme.get('name'),
                            'external_subcategory_id': subcategory.get('id'),
                            'subcategory_name': subcategory.get('name'),
                            'external_category_id': category.get('id'),
                            'category_name': category.get('name'),
                            'url': (
                                'https://investmoscow.ru/business/'
                                'moscow-investor-request'
                                f'?problem={external_id}'
                            ),
                        },
                    )
                    logger.info(f'Обработана запись: {problem.name}')
