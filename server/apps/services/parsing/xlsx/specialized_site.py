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
from server.apps.services.parsing.xlsx.base import (
    ObjectType,
    clear_data,
    get_correct_data,
)
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
                is_possibility_redemption = (
                    False
                    if row[14] and row[14].lower() == 'нет'
                    else True
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
                    for economic_activity_row_data in row[15].split(';'):
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
                                    'name': re.sub('\xa0', '', re.sub('\xa0', '', '-'.join(economic_activity_data[1:]))),
                                },
                            )
                        if created:
                            specialized_site.economic_activities.add(industry.id)

                # Ограничения по видам деятельности.
                if row[16]:
                    for restriction_row_data in row[16].split('\n\n'):
                        restriction, created = Restriction.objects.get_or_create(
                            name=restriction_row_data,
                        )
                        if created:
                            specialized_site.restrictions.add(restriction.id)

                # Инфраструктура и сервисы.
                if row[17]:
                    for infrastructure_row_data in row[17].split('\n'):
                        infrastructure, created = Infrastructure.objects.get_or_create(
                            name=infrastructure_row_data,
                        )
                        if created:
                            specialized_site.infrastructures.add(infrastructure.id)
                # Льготы
                if row[28]:
                    for privilege_row_data in row[28].split('\n'):
                        privilege, created = Privilege.objects.get_or_create(
                            name=privilege_row_data,
                        )
                        if created:
                            specialized_site.privileges.add(privilege.id)

                logger.info(f'Завершена обработка {row[3]}')

