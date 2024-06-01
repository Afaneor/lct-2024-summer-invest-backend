from server.apps.hincal.models import (
    Business,
    Sector,
    SubSector,
    TerritorialLocation,
)
from server.apps.hincal.services.enums import TypeBusiness
from server.apps.user.models import User
from server.apps.user.services.create_business import (
    HANDLER_TERRITORIAL_LOCATION,
    get_business_by_inn,
)
from server.celery import app


@app.task(bind=True)
def create_business(self, inn: str, user_id: int) -> None:
    """Выбираем нужную информацию о компании или ИП и сохраняем ее в БД.

    Информация берется из DaData.
    """
    user = User.objects.get(id=user_id)
    business_information = get_business_by_inn(inn=inn)
    sector = Sector.objects.get(slug='other')
    sub_sector = SubSector.objects.get(slug='other')
    if business_information:
        business = business_information[0]
        data = business.get('data', {})
        address = data.get('address', {})
        territorial_location = TerritorialLocation.objects.get(
            slug=HANDLER_TERRITORIAL_LOCATION.get(
                address.get('data', {}).get('city_area', '').lower(),
            ),
        )
        Business.objects.create(
            type=data.get('type').lower(),
            inn=inn,
            territorial_location=territorial_location,
            hid=data.get('hid', ''),
            short_business_name=data.get('name', {}).get('short_with_opf', ''),
            full_business_name=data.get('name', {}).get('full_with_opf', ''),
            management_name=data.get('management', {}).get('name', ''),
            management_position=data.get('management', {}).get('post', ''),
            full_opf=data.get('opf', {}).get('full', ''),
            short_opf=data.get('opf', {}).get('short', ''),
            okved=data.get('okved', ''),
            first_name=data.get('fio', {}).get('name', ''),
            last_name=data.get('fio', {}).get('surname', ''),
            middle_name=data.get('fio', {}).get('patronymic', ''),
            address=address.get('unrestricted_value', ''),
            country=address.get('data', {}).get('country', ''),
            region=address.get('data', {}).get('region', ''),
            city_area=address.get('data', {}).get('city_area', ''),
            city_district=address.get('data', {}).get('city_district', ''),
            phone=data.get('phones', {})[0].get('value', ''),
            email=data.get('phones', {})[0].get('value', ''),
            sector=sector,
            sub_sector=sub_sector,
        )
    else:
        Business.objects.create(
            type=TypeBusiness.PHYSICAL,
            inn=inn,
            first_name=user.first_name,
            last_name=user.last_name,
            middle_name=user.middle_name,
            sector=sector,
            sub_sector=sub_sector,
        )
