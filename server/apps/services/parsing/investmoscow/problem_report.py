import logging

import requests

from server.apps.services.parsing.xlsx.base import clear_data, get_correct_data
from server.apps.support.models import (
    Problem,
    ProblemCategory,
    ProblemSubcategory,
    ProblemTheme,
)

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
    for category_data in response.json():
        problem_category, pc_created = ProblemCategory.objects.get_or_create(
            external_id=clear_data(category_data.get('id')),
            name=get_correct_data(category_data.get('name')),
        )
        for subcategory_data in category_data.get('subcategories', []):
            problem_subcategory, ps_created = ProblemSubcategory.objects.get_or_create(
                problem_category=problem_category,
                external_id=clear_data(subcategory_data.get('id')),
                name=get_correct_data(subcategory_data.get('name')),
            )
            for theme_data in subcategory_data.get('themes', []):
                problem_theme, pt_created = ProblemTheme.objects.get_or_create(
                    problem_subcategory=problem_subcategory,
                    external_id=clear_data(theme_data.get('id')),
                    name=get_correct_data(theme_data.get('name')),
                )
                for problem_data in theme_data.get('problems', []):
                    external_id = clear_data(problem_data.get('id'))
                    problem_report, p_created = Problem.objects.get_or_create(
                        problem_theme=problem_theme,
                        external_id=external_id,
                        name=get_correct_data(problem_data.get('name')),
                        url=(
                            'https://investmoscow.ru/business/'
                            'moscow-investor-request'
                            f'?problem={external_id}'
                        ),
                    )
                    logger.info(f'Обработана запись: {problem_report.name}')
