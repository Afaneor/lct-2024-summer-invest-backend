# from typing import Dict
#
# import requests
#
# from server.apps.investment_site.models.extra_data import ExtraData
# from server.apps.investment_site.models.building import Building
# from server.apps.investment_site.models.contact import Contact
# from server.apps.investment_site.models.engineering_infrastructure import \
#     EngineeringInfrastructure
# from server.apps.investment_site.models.investment_site import \
#     InvestmentSite
# from server.apps.investment_site.models.land_plot import LandPlot
# from server.apps.investment_site.models.room_for_rent import RoomForRent
# from server.apps.investment_site.models.tender import Tender
#
# URL_MAPPING: Dict[int, str] = {
#     # ТЕХНОПАРКИ. https://investmoscow.ru/business/technoparks
#     1: 'https://api.investmoscow.ru/investmoscow/industry/v1/techpark/get?id={id}',
#     # ПЛОЩАДКИ ОЭЗ "ТЕХНОПОЛИC".
#     # https://investmoscow.ru/business/sez-technopolis-moscow
#     2: 'https://api.investmoscow.ru/investmoscow/industry/v1/economiczone/getseztechnopolismoscowsite?id={id}',
#     # ИНВЕСТИЦИОННЫЙ КАТАЛОГ. https://investmoscow.ru/business/invest-catalog
#     3: 'https://api.investmoscow.ru/investmoscow/industry/v1/investcatalog/getobject?id={id}',
#     # РЕЕСТР ПРОМПЛОЩАДОК. https://investmoscow.ru/business/site-list
#     4: 'https://api.investmoscow.ru/investmoscow/industry/v1/industryzone/getroomforindustrial?id={id}',
#     # РЕЕСТР ПРОМПЛОЩАДОК. ЗЕМЕЛЬНЫЕ УЧАСТКИ.
#     # https://investmoscow.ru/business/site-list
#     5: 'https://api.investmoscow.ru/investmoscow/industry/v1/industryzone/getroomforindustrial?id={id}',
#     6: 'https://api.investmoscow.ru/investmoscow/industry/v1/krt/getById?id={id}'
# }
#
# ''
#
#
# def parsing_technopolis_1(
#     investment_site: InvestmentSite,
#     extra_data: ExtraData,
# ):
#     """Парсинг технопарков."""
#     # Формируем запрос к api.
#     url_for_parsing = URL_MAPPING.get(
#         investment_site.investment_object_type,
#     ).format(
#         id=investment_site.investment_site_id,
#     )
#     response_json = requests.get(
#         url=url_for_parsing,
#         headers={'Content-Type': 'application/json'},
#     ).json()
#
#     extra_data.general_info = response_json.get(
#         'genericInfoTab',
#     ).get(
#         'generalInfo',
#     )
#     extra_data.save(update_fields=['general_info'])
#
#     # Добавляем фотографии, если они есть
#     investment_site.photo_urls = response_json.get('photoUrls')
#     investment_site.save(update_fields=['photo_urls'])
#
#     # Добавляем инженерную инфраструктуру.
#     engineering_infrastructure = response_json.get(
#         'engineeringInfrastructureTab',
#     )
#     EngineeringInfrastructure.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'heating_supply_free_power':
#                 engineering_infrastructure.get('heatingSupplyFreePower'),
#             'heating_supply_max_available_power':
#                 engineering_infrastructure.get('heatingSupplyMaxAvailablePower'),  # noqa: E501
#             'power_supply_free_power':
#                 engineering_infrastructure.get('powerSupplyFreePower'),
#             'power_supply_max_available_power':
#                 engineering_infrastructure.get('powerSupplyMaxAvailablePower'),
#             'sewers_free_power':
#                 engineering_infrastructure.get('sewersFreePower'),
#             'sewers_max_available_power':
#                 engineering_infrastructure.get('sewersMaxAvailablePower'),
#             'water_supply_free_power':
#                 engineering_infrastructure.get('waterSupplyFreePower'),
#             'water_supply_max_available_power':
#                 engineering_infrastructure.get('waterSupplyMaxAvailablePower'),
#         },
#     )
#
#     contact_json = response_json.get('contactInfoTab')
#     Contact.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'address': contact_json.get('address'),
#             'contact_person': contact_json.get('contactPerson'),
#             'management_company': contact_json.get('managementCompany'),
#             'phone': contact_json.get('phone'),
#             'url': contact_json.get('url'),
#         },
#     )
#
#
# def parsing_technopolis_2(
#     investment_site: InvestmentSite,
#     extra_data: ExtraData,
# ):
#     """Парсинг технополисов."""
#     # Формируем запрос к api.
#     url_for_parsing = URL_MAPPING.get(
#         investment_site.investment_object_type,
#     ).format(
#         id=investment_site.investment_site_id,
#     )
#     response_json = requests.get(
#         url=url_for_parsing,
#         headers={'Content-Type': 'application/json'},
#     ).json()
#
#     # Обновляем дополнительную информацию об объекте.
#     extra_data_json = response_json.get('genericInfoTab')
#
#     extra_data.investment_size = extra_data_json.get('investmentSize')
#     extra_data.okrug = extra_data_json.get('okrug')
#     extra_data.residents_count = extra_data_json.get('residentsCount')
#     extra_data.workplaces_count = extra_data_json.get('workplacesCount')
#
#     extra_data.save(
#         update_fields=[
#             'investment_size',
#             'okrug',
#             'residents_count',
#             'workplaces_count',
#         ],
#     )
#
#     # Добавляем фотографии, если они есть
#     investment_site.photo_urls = response_json.get('photoUrls')
#     investment_site.save(update_fields=['photo_urls'])
#
#     # Добавляем инженерную инфраструктуру.
#     engineering_infrastructure = response_json.get(
#         'engineeringInfrastructureTab',
#     )
#     EngineeringInfrastructure.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'heating_supply_free_power':
#                 engineering_infrastructure.get('heatingSupplyFreePower'),
#             'heating_supply_max_available_power':
#                 engineering_infrastructure.get('heatingSupplyMaxAvailablePower'),  # noqa: E501
#             'power_supply_free_power':
#                 engineering_infrastructure.get('powerSupplyFreePower'),
#             'power_supply_max_available_power':
#                 engineering_infrastructure.get('powerSupplyMaxAvailablePower'),
#             'sewers_free_power':
#                 engineering_infrastructure.get('sewersFreePower'),
#             'sewers_max_available_power':
#                 engineering_infrastructure.get('sewersMaxAvailablePower'),
#             'water_supply_free_power':
#                 engineering_infrastructure.get('waterSupplyFreePower'),
#             'water_supply_max_available_power':
#                 engineering_infrastructure.get('waterSupplyMaxAvailablePower'),
#         },
#     )
#
#
# def parsing_technopark_3(
#     investment_site: InvestmentSite,
# ):
#     """Парсинг технопарков."""
#     # Формируем запрос к api.
#     url_for_parsing = URL_MAPPING.get(
#         investment_site.investment_object_type,
#     ).format(
#         id=investment_site.investment_site_id,
#     )
#     response_json = requests.get(
#         url=url_for_parsing,
#         headers={'Content-Type': 'application/json'},
#     ).json()
#
#     # Добавляем фотографии, если они есть
#     investment_site.photo_urls = response_json.get('photoUrls')
#     investment_site.save(update_fields=['photo_urls'])
#
#     building_json = response_json.get('buildingTab')
#     Building.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'area': building_json.get('area'),
#             'count': building_json.get('count'),
#             'year': building_json.get('year'),
#         },
#     )
#
#     land_plot_json = response_json.get('landPlotTab')
#     LandPlot.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'area': land_plot_json.get('area'),
#             'area_unit': land_plot_json.get('areaUnit'),
#             'cadastral_number': land_plot_json.get('cadastralNumber'),
#             'gpzu_date': land_plot_json.get('gpzuDate'),
#             'gpzu_number': land_plot_json.get('gpzuNumber'),
#             'vri': land_plot_json.get('vri'),
#         },
#     )
#
#
# def parsing_industrial_site_4(
#     investment_site: InvestmentSite,
#     extra_data: ExtraData,
# ):
#     """Парсинг промплощадок."""
#     # Формируем запрос к api.
#     url_for_parsing = URL_MAPPING.get(
#         investment_site.investment_object_type,
#     ).format(
#         id=investment_site.investment_site_id,
#     )
#     response_json = requests.get(
#         url=url_for_parsing,
#         headers={'Content-Type': 'application/json'},
#     ).json()
#
#     # Обновляем дополнительную информацию об объекте.
#     extra_data_json = response_json.get('genericInfoTab')
#
#     extra_data.address = extra_data_json.get('address')
#     extra_data.general_info = extra_data_json.get('desc')
#     extra_data.ground_area = extra_data_json.get('groundArea')
#     extra_data.okrug = extra_data_json.get('okrug')
#
#     extra_data.save(
#         update_fields=[
#             'address',
#             'general_info',
#             'ground_area',
#             'okrug',
#         ],
#     )
#
#     # Добавляем фотографии, если они есть
#     investment_site.photo_urls = response_json.get('photoUrls')
#     investment_site.save(update_fields=['photo_urls'])
#
#     room_for_rent_json = response_json.get('roomForRentTab')
#     RoomForRent.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'area': room_for_rent_json.get('area'),
#             'electricity': room_for_rent_json.get('electricity'),
#             'heating': room_for_rent_json.get('heating'),
#             'parking': room_for_rent_json.get('parking'),
#             'price': room_for_rent_json.get('price'),
#             'room_type': room_for_rent_json.get('type'),
#             'water': room_for_rent_json.get('water'),
#         },
#     )
#
#
# def parsing_industrial_site_5(
#     investment_site: InvestmentSite,
#     extra_data: ExtraData,
# ):
#     """Парсинг промплощадок (земельных участков)."""
#     # Формируем запрос к api.
#     url_for_parsing = URL_MAPPING.get(
#         investment_site.investment_object_type,
#     ).format(
#         id=investment_site.investment_site_id,
#     )
#     response_json = requests.get(
#         url=url_for_parsing,
#         headers={'Content-Type': 'application/json'},
#     ).json()
#
#     # Обновляем дополнительную информацию об объекте.
#     extra_data_json = response_json.get('genericInfoTab')
#
#     extra_data.address = extra_data_json.get('address')
#     extra_data.cadastral_number = extra_data_json.get('cadastrNumber')
#     extra_data.general_info = extra_data_json.get('desc')
#     extra_data.ground_area = extra_data_json.get('groundArea')
#     extra_data.okrug = extra_data_json.get('okrug')
#
#     extra_data.save(
#         update_fields=[
#             'address',
#             'general_info',
#             'ground_area',
#             'okrug',
#         ],
#     )
#
#     # Добавляем фотографии, если они есть
#     investment_site.photo_urls = response_json.get('photoUrls')
#     investment_site.save(update_fields=['photo_urls'])
#
#     room_for_rent_json = response_json.get('roomForRentTab')
#     RoomForRent.objects.get_or_create(
#         investment_site=investment_site,
#         defaults={
#             'area': room_for_rent_json.get('area'),
#             'electricity': room_for_rent_json.get('electricity'),
#             'heating': room_for_rent_json.get('heating'),
#             'parking': room_for_rent_json.get('parking'),
#             'price': room_for_rent_json.get('price'),
#             'room_type': room_for_rent_json.get('type'),
#             'water': room_for_rent_json.get('water'),
#         },
#     )
#
#
# def parsing_tender(
#
# ):
#     # Формируем запрос к api для получения списка всех объектов на продажу.
#     all_tender_json = requests.post(
#         url='https://api.investmoscow.ru/investmoscow/investment-map/v1/tenderObject/searchTenderObjectsShort',
#         headers={'Content-Type': 'application/json'},
#         json={
#             'PageNumber': 1,
#             'PageSize': 10000,
#         },
#     ).json()
#     for entity in all_tender_json['entities']:
#         tender_id = entity['tenderId']
#         tender_url = (
#             'https://api.investmoscow.ru/investmoscow/tender/v1/object-info/'
#             f'gettenderobjectinformation?tenderId={tender_id}'
#         )
#         tender_json = requests.get(
#             url=tender_url,
#             headers={'Content-Type': 'application/json'},
#         ).json()
#
#         photo_urls = [
#             photo.get('url')
#             for photo in tender_json.get('imageInfo', {}).get('attachedImages')
#         ]
#
#         Tender.objects.get_or_create(
#             tender_id=tender_id,
#             object_type_id=tender_json['objectTypeId'],
#             detail_url=tender_url,
#             all_docs_link=tender_json.get(
#                 'documentInfo',
#                 {},
#             ).get(
#                 'allDocsArchiveDownloadLink',
#             ),
#             photo_urls=photo_urls,
#             latitude=tender_json['mapInfo']['coords']['lat'],
#             longitude=tender_json['mapInfo']['coords']['long'],
#         )
