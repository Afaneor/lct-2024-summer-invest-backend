import logging
import re

import pylightxl as xl

from server.apps.investment_object.models import (
    Infrastructure,
    InvestmentObject,
    SpecializedSite,
)
from server.apps.investment_object.models.economic_activity import (
    EconomicActivity,
)
from server.apps.investment_object.models.privilege import Privilege
from server.apps.investment_object.models.restriction import Restriction
from server.apps.investment_object.services.enums import ObjectType
from server.apps.services.parsing.xlsx.base import clear_data, get_correct_data
from server.settings.components import BASE_DIR

logger = logging.getLogger('django')


def parsing_specialized_site():
    """
    Парсинг технополисов и технопарков из файла.
    """
    db = xl.readxl(
        f'{BASE_DIR}'
        '/server/apps/investment_object/initial_data/specialized_site.xlsx'
    )
    for list_name in db.ws_names:
        for index, row in enumerate(db.ws(ws=list_name).rows):
            if index != 0:
                row = list(map(clear_data, row))
                object_type = (
                    ObjectType.TECHNOPOLIS.value
                    if row[0] and row[0] == 'Особая экономическая зона'
                    else ObjectType.TECHNOPARK.value
                )
                validity = (
                    int(row[11])
                    if row[11] and len(row[11].split('.')) == 1
                    else int(row[11].split('.')[-1]) - int(row[10])
                )
                transaction_form = (
                    'Выкуп помещения/участка не возможен'
                    if row[14] and row[14].lower() == 'нет'
                    else 'Возможен выкуп помещения/участка'
                )
                is_free_customs_zone_regime = (
                    False
                    if row[29] and row[29].lower() == 'нет'
                    else True
                )

                if row[8]:
                    photo_urls = row[8].split('\n')
                    main_photo_url = photo_urls[0]
                else:
                    photo_urls = []
                    main_photo_url = ''

                investment_object, io_created = InvestmentObject.objects.get_or_create(
                    name=row[3],
                    defaults={
                        'main_photo_url': main_photo_url,
                        'photo_urls': photo_urls,
                        'object_type': object_type,
                    },
                )
                specialized_site, ss_created = SpecializedSite.objects.update_or_create(
                    investment_object=investment_object,
                    defaults={
                        'sez': get_correct_data(row[1]),
                        'tad': get_correct_data(row[2]),
                        'name': get_correct_data(row[3]),
                        'region': get_correct_data(row[4]),
                        'municipality': get_correct_data(row[5]),
                        'nearest_cities': get_correct_data(row[6]),
                        'number_residents': int(row[7]) if row[7] else None,
                        'document_url': (
                            re.sub('[\n\t\r]', '', row[9].strip())
                            if row[9]
                            else ''
                        ),
                        'year_formation': int(row[10]) if row[10] else None,
                        'validity': validity,
                        'minimum_rental_price': (
                            row[12].replace(',', '.')
                            if row[12]
                            else None
                        ),
                        'total_area': (
                            row[13].replace(',', '.')
                            if row[13]
                            else None
                        ),
                        'is_possibility_redemption': is_possibility_redemption,
                        'additional_services': get_correct_data(row[18]),
                        'object_administrator_name': get_correct_data(row[19]),
                        'address': get_correct_data(row[20]),
                        'website': get_correct_data(row[21]),
                        'working_hours': get_correct_data(row[22]),
                        'income_tax': get_correct_data(row[23]),
                        'property_tax': get_correct_data(row[24]),
                        'land_tax': get_correct_data(row[25]),
                        'transport_tax': get_correct_data(row[26]),
                        'insurance_premiums': get_correct_data(row[27]),
                        'is_free_customs_zone_regime':
                            is_free_customs_zone_regime,
                        'resident_info': get_correct_data(row[30]),
                        'minimum_investment_amount': get_correct_data(row[31]),
                        'longitude': row[32].split(',')[0] if row[32] else None,
                        'latitude': row[32].split(',')[1] if row[32] else None,
                    },
                )

                # Список отраслей.
                if row[15]:
                    objects_for_add = []
                    for economic_activity_row_data in row[15].split(';'):
                        economic_activity_data = economic_activity_row_data.split('-')
                        if economic_activity_data[0].strip().lower() == 'нет ограничений':
                            economic_activity, created = EconomicActivity.objects.get_or_create(
                                code=economic_activity_data[0].strip(),
                                defaults={
                                    'name': economic_activity_data[0].strip(),
                                },
                            )
                        else:
                            economic_activity, created = EconomicActivity.objects.get_or_create(
                                code=economic_activity_data[0].strip(),
                                defaults={
                                    'name': re.sub('\xa0', '', re.sub('\xa0', '', '-'.join(economic_activity_data[1:]))).strip(),
                                },
                            )

                        objects_for_add.append(economic_activity)
                    specialized_site.economic_activities.set(objects_for_add)

                # Ограничения по видам деятельности.
                if row[16]:
                    objects_for_add = []
                    for restriction_row_data in row[16].split('\n\n'):
                        restriction, created = Restriction.objects.get_or_create(
                            name=restriction_row_data,
                        )
                        objects_for_add.append(restriction)
                    specialized_site.restrictions.set(objects_for_add)

                # Инфраструктура и сервисы.
                if row[17]:
                    objects_for_add = []
                    for infrastructure_row_data in row[17].split('\n'):
                        infrastructure, created = Infrastructure.objects.get_or_create(
                            name=infrastructure_row_data.replace('• ', ''),
                        )
                        objects_for_add.append(infrastructure)
                    specialized_site.infrastructures.set(objects_for_add)
                # Льготы
                if row[28]:
                    objects_for_add = []
                    for privilege_row_data in row[28].split('\n'):
                        privilege, created = Privilege.objects.get_or_create(
                            name=privilege_row_data,
                        )
                        objects_for_add.append(privilege)
                    specialized_site.privileges.set(objects_for_add)

                logger.info(f'Завершена обработка {row[3]}')

