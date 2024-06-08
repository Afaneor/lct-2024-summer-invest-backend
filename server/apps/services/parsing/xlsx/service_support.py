import logging
import re

import pylightxl as xl

from server.apps.investment_object.models.economic_activity import (
    EconomicActivity,
)
from server.apps.investment_object.models.restriction import Restriction
from server.apps.services.parsing.xlsx.base import get_correct_data
from server.apps.support.models import ServiceSupport
from server.apps.support.services.enums import TypeServiceSupport
from server.settings.components import BASE_DIR

logger = logging.getLogger('django')


def parsing_service_support():
    """
    Парсинг мер поддержки.
    """
    db = xl.readxl(
        f'{BASE_DIR}'
        '/server/apps/investment_object/initial_data/support.xlsx'
    )
    for list_name in db.ws_names:
        for index, row in enumerate(db.ws(ws=list_name).rows):
            if index != 0:
                is_msp_roster = (
                    False
                    if row[13].lower() == 'нет'
                    else True
                )
                support, s_created = ServiceSupport.objects.update_or_create(
                    name=row[1],
                    defaults={
                        'region': get_correct_data(row[0]),
                        'type_service_support': TypeServiceSupport.SUPPORT_MEASURE,
                        'support_type': get_correct_data(row[2]).lower(),
                        'support_level': get_correct_data(row[3]).lower(),
                        'description': get_correct_data(row[4]),
                        'legal_act': get_correct_data(row[5]),
                        'url_legal_act': get_correct_data(row[6]),
                        'url_application_form': get_correct_data(row[8]),
                        'name_responsible_body': get_correct_data(row[9]),
                        'is_msp_roster': is_msp_roster,
                        'applicant_requirement': get_correct_data(row[14]),
                        'applicant_procedure': get_correct_data(row[15]),
                        'required_document': get_correct_data(row[16]),
                    },
                )
                if row[11]:
                    for economic_activity_row_data in row[11].split(';'):
                        economic_activity_data = economic_activity_row_data.split('-')
                        if economic_activity_data[0].strip().lower() == 'нет ограничений':
                            industry, created = EconomicActivity.objects.get_or_create(
                                code=economic_activity_data[0].strip(),
                                defaults={
                                    'name': economic_activity_data[0].strip(),
                                },
                            )
                        else:
                            industry, created = EconomicActivity.objects.get_or_create(
                                code=economic_activity_data[0].strip(),
                                defaults={
                                    'name': re.sub('\xa0', '', '-'.join(economic_activity_data[1:])),
                                },
                            )
                        if created:
                            support.economic_activities.add(industry)

                if row[12]:
                    for restriction_row_data in row[12].split(';'):
                        restriction, created = Restriction.objects.get_or_create(
                            name=restriction_row_data,
                        )
                        if created:
                            support.restrictions.add(restriction)

            logger.info(f'Завершена обработка {row[1]}')
