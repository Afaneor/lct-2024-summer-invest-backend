import logging

import requests

from server.apps.services.parsing.xlsx.base import clear_data, get_correct_data
from server.apps.support.models import ServiceProblem

logger = logging.getLogger('django')


def parsing_problem_report():
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
                    problem_report, created = ServiceProblem.objects.get_or_create(
                        external_id=problem.get('id'),
                        defaults={
                            'name': get_correct_data(problem.get('name')),
                            'additional_info':
                                get_correct_data(problem.get('faq')),
                            'external_theme_id': clear_data(theme.get('id')),
                            'theme_name': get_correct_data(theme.get('name')),
                            'external_subcategory_id':
                                clear_data(subcategory.get('id')),
                            'subcategory_name':
                                get_correct_data(subcategory.get('name')),
                            'external_category_id':
                                clear_data(category.get('id')),
                            'category_name':
                                get_correct_data(category.get('name')),
                            'url': (
                                'https://investmoscow.ru/business/'
                                'moscow-investor-request'
                                f'?problem={external_id}'
                            ),
                        },
                    )
                    logger.info(f'Обработана запись: {problem_report.name}')
