import re
from typing import Any, Dict, List

import pylightxl as xl

from server.apps.investment_object.models import (
    InvestmentObject,
    SpecializedSite,
)
from server.apps.investment_object.models.economic_activity import (
    EconomicActivity,
)
from server.apps.investment_object.models.infrastructure import Infrastructure
from server.apps.investment_object.models.privilege import Privilege
from server.apps.investment_object.models.real_estate import RealEstate
from server.apps.investment_object.models.restriction import Restriction
from server.apps.support.models import Support


class ObjectType(models.Model):
    """
    Типы объектов.
    """

    TECHNOPARK = 'technopark'
    TECHNOPOLIS = 'technopolis'
    LAND = 'land'
    BUILDING = 'building'


def parsing_specialized_site():
    """
    Парсинг технополисов и технопарков из файла.
    """
    db = xl.readxl(
        '/server/apps/investment_object/initial_data/specialized_site.xlsx')
    for list_name in db.ws_names:
        for index, row in enumerate(db.ws(ws=list_name).rows):
            if index != 0:
                object_type = (
                    ObjectType.TECHNOPOLIS
                    if row[0] == 'Особая экономическая зона'
                    else ObjectType.TECHNOPARK
                )
                validity = (
                    row[11]
                    if len(row[11].split('.')) == 1
                    else int(row[11].split('.')[-1]) - int(row[10])
                )
                is_possibility_redemption = (
                    False
                    if row[14].lower() == 'нет'
                    else True
                )
                is_free_customs_zone_regime = (
                    False
                    if row[29].lower() == 'нет'
                    else True
                )
                investment_object, io_created = InvestmentObject.objects.get_or_create(
                    name=row[1],
                    defaults={
                        'main_photo_url': row[8].split('\n')[0],
                        'photo_urls': row[8].split('\n'),
                        'object_type': object_type,
                    },
                )
                specialized_site, ss_created = SpecializedSite.objects.update_or_create(
                    investment_object=investment_object,
                    defaults={
                        'sez': row[1],
                        'tad': row[2],
                        'name': row[3],
                        'region': row[4],
                        'municipality': row[5],
                        'nearest_cities': row[6],
                        'number_residents': row[7],
                        'document_url': re.sub('[\n\t\r]', '', row[9].strip()),
                        'year_formation': int(row[10]) if row[10] else None,
                        'validity': validity,
                        'total_area': row[12],
                        'minimum_rental_price': row[13],
                        'is_possibility_redemption': is_possibility_redemption,
                        'additional_services': row[18],
                        'object_administrator_name': row[19],
                        'address': row[20],
                        'website': row[21],
                        'working_hours': row[22],
                        'income_tax': row[23],
                        'property_tax': row[24],
                        'land_tax': row[25],
                        'transport_tax': row[26],
                        'insurance_premiums': row[27],
                        'is_free_customs_zone_regime': is_free_customs_zone_regime,
                        'resident_info': row[30],
                        'minimum_investment_amount': row[31],
                        'longitude': row[32].split('.')[0],
                        'latitude': row[32].split('.')[1],
                    },
                )
                for economic_activity_row_data in row[15].split(':'):
                    economic_activity_data = economic_activity_row_data.split(' - ')
                    industry, created = EconomicActivity.objects.get_or_create(
                        code=economic_activity_data[0],
                        name=economic_activity_data[1],
                    )
                    if created:
                        specialized_site.industries.add(industry)

                for restriction_row_data in row[16].split('\n\n'):
                    restriction, created = Restriction.objects.get_or_create(
                        name=restriction_row_data,
                    )
                    if created:
                        specialized_site.restrictions.add(restriction)

                for infrastructure_row_data in row[17].split('\n'):
                    infrastructure, created = Infrastructure.objects.get_or_create(
                        name=infrastructure_row_data,
                    )
                    if created:
                        specialized_site.infrastructures.add(infrastructure)

                for privilege_row_data in row[28].split('\n'):
                    infrastructure, created = Privilege.objects.get_or_create(
                        name=privilege_row_data,
                    )
                    if created:
                        specialized_site.infrastructures.add(infrastructure)




def parsing_real_estate():
    """
    Парсинг зданий и сооружений.
    """
    db = xl.readxl(
        '/server/apps/investment_object/initial_data/real_estate.xlsx')
    for list_name in db.ws_names:
        for index, row in enumerate(db.ws(ws=list_name).rows):
            if index != 0:
                object_type = (
                    ObjectType.BUILDING
                    if row[11] == 'Помещение'
                    else ObjectType.LAND
                )
                is_cupping = (
                    False
                    if row[25].lower() == 'нет'
                    else True
                )
                is_maip = (
                    False
                    if row[81].lower() == 'нет'
                    else True
                )
                investment_object, io_created = InvestmentObject.objects.get_or_create(
                    name=row[0],
                    defaults={
                        'main_photo_url': row[83].split('\n')[0],
                        'photo_urls': row[83].split('\n'),
                        'object_type': object_type,
                    },
                )
                real_estate, re_created = RealEstate.objects.update_or_create(
                    investment_object=investment_object,
                    defaults={
                        'preferential_treatment': row[1],
                        'preferential_treatment_object_code': row[2],
                        'preferential_treatment_object_name': row[3],
                        'support_infrastructure_object': row[4],
                        'support_infrastructure_object_code': row[5],
                        'support_infrastructure_object_name': row[6],
                        'region': row[7],
                        'municipality': row[8],
                        'address': row[9],
                        'nearest_cities': row[10],
                        'redevelopment_type': row[12],
                        'ownership_type': row[13],
                        'form_transaction': row[14],
                        'object_cost': row[15],
                        'rental_period': row[18],
                        'procedure_determining_cost': row[19],
                        'hazard_class_object': row[20],
                        'characteristic_object': row[21],
                        'land_free_area': row[22],
                        'land_cadastral_number': row[23],
                        'permitted_use_options': row[24],
                        'is_cupping': is_cupping,
                        'land_category': row[26],
                        'building_free_area': row[27],
                        'building_cadastral_number': row[28],
                        'building_technical_specifications': row[29],
                        'owner_name': row[30],
                        'owner_inn': row[31],
                        'owner_website': row[32],
                        'other_characteristics': row[82],
                        'application_procedure': row[76],
                        'documents_for_application': row[77],
                        'application_form_url': row[78],
                        'urban_planning': row[80],
                        'is_maip': is_maip,
                        'benefit_description': row[82],
                        'longitude': row[83].split('.')[0],
                        'latitude': row[83].split('.')[1],
                    }
                )

                if row[34].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[34].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_water_supply = create_infrastructure(
                        row=row,
                        start_number_row=35,
                        name='Водоснабжение',
                        unit_measure='руб./куб. м',
                        availability=availability,
                    )

                    real_estate.infrastructures.add(infrastructure_water_supply)

                if row[41].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[41].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_sewage = create_infrastructure(
                        row=row,
                        start_number_row=42,
                        name='Водоотведение',
                        unit_measure='руб./куб. м',
                        availability=availability,
                    )

                    real_estate.infrastructures.add(infrastructure_sewage)

                if row[48].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[48].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_gas = create_infrastructure(
                        row=row,
                        start_number_row=49,
                        name='Газоснабжение',
                        unit_measure='руб./куб. м',
                        availability=availability,
                    )

                    real_estate.infrastructures.add(infrastructure_gas)

                if row[55].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[55].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_electricity = create_infrastructure(
                        row=row,
                        start_number_row=56,
                        name='Электроснабжение',
                        unit_measure='руб./МВт*ч',
                        availability=availability,
                    )

                    real_estate.infrastructures.add(infrastructure_electricity)

                if row[62].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[62].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_heat = create_infrastructure(
                        row=row,
                        start_number_row=63,
                        name='Теплоснабжение',
                        unit_measure='руб./Гкал*ч',
                        availability=availability,
                    )

                    real_estate.infrastructures.add(infrastructure_heat)

                if row[69].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[69].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_tko = Infrastructure.objects.create(
                        name='Вывоз ТКО',
                        consumption_tariff=(
                            f'{row[71]}  руб./куб. м'
                            if row[71]
                            else None
                        ),
                        availability=availability
                    )

                    real_estate.infrastructures.add(infrastructure_tko)

                if row[72].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[72].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_access_roads = Infrastructure.objects.create(
                        name='Подъездные пути',
                        availability=availability
                    )

                    real_estate.infrastructures.add(infrastructure_access_roads)

                if row[73].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[73].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_railroad_tracks = Infrastructure.objects.create(
                        name='Ж/д пути',
                        availability=availability
                    )

                    real_estate.infrastructures.add(infrastructure_railroad_tracks)

                if row[74].lower() != 'нет':
                    availability = (
                        InfrastructureAvailability.YES
                        if row[74].lower() == 'да'
                        else InfrastructureAvailability.POSSIBLE_CREATION
                    )
                    infrastructure_availability_truck_parking = Infrastructure.objects.create(
                        name='Наличие парковки грузового транспорт',
                        availability=availability
                    )

                    real_estate.infrastructures.add(infrastructure_availability_truck_parking)


                for economic_activity_row_data in row[79].split(':'):
                    economic_activity_data = economic_activity_row_data.split(' - ')
                    industry, created = EconomicActivity.objects.get_or_create(
                        code=economic_activity_data[0],
                        name=economic_activity_data[1],
                    )
                    if created:
                        real_estate.industries.add(industry)


def create_infrastructure(
    row,
    start_number_row: int,
    name: str,
    unit_measure: str,
    availability: str,
):
    return Infrastructure.objects.create(
        name=name,
        consumption_tariff=(
            f'{row[start_number_row]} {unit_measure}'
            if row[start_number_row]
            else None
        ),
        transportation_tariff=(
            f'{row[start_number_row+1]} {unit_measure}'
            if row[start_number_row+1]
            else None
        ),
        max_allowable_power=(
            f'{row[start_number_row+2]} {unit_measure}'
            if row[start_number_row+2]
            else None
        ),
        free_power=(
            f'{row[start_number_row+3]} {unit_measure}'
            if row[start_number_row+3]
            else None
        ),
        throughput=(
            f'{row[start_number_row+5]} {unit_measure}'
            if row[start_number_row+5]
            else None
        ),
        other_characteristics=row[start_number_row+4],
        availability=availability
    )


def parsing_support():
    """
    Парсинг мер поддержки.
    """
    db = xl.readxl('/server/apps/investment_object/initial_data/support.xlsx')
    for list_name in db.ws_names:
        for index, row in enumerate(db.ws(ws=list_name).rows):
            if index != 0:
                is_msp_roster = (
                    False
                    if row[13].lower() == 'нет'
                    else True
                )
                support, s_created = Support.objects.update_or_create(
                    name=row[1],
                    defaults={
                        'region': row[0],
                        'support_type': row[2].lower(),
                        'support_level': row[3].lower(),
                        'description': row[4],
                        'legal_act': row[5],
                        'url_legal_act': row[6],
                        'application_form_link': row[8],
                        'name_responsible_body': row[9],
                        'is_msp_roster': is_msp_roster,
                        'applicant_requirement': row[14],
                        'applicant_procedure': row[15],
                        'required_document': row[16],
                    },
                )
                for economic_activity_row_data in row[11].split(':'):
                    economic_activity_data = economic_activity_row_data.split(' - ')
                    industry, created = EconomicActivity.objects.get_or_create(
                        code=economic_activity_data[0],
                        name=economic_activity_data[1],
                    )
                    if created:
                        support.industries.add(industry)

                for restriction_row_data in row[12].split('\n\n'):
                    restriction, created = Restriction.objects.get_or_create(
                        name=restriction_row_data,
                    )
                    if created:
                        support.restrictions.add(restriction)
