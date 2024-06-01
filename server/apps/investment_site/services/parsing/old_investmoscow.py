# from typing import Dict, Any
#
# import requests
#
# from server.apps.investment_site.models.extra_data import ExtraData
# from server.apps.investment_site.models.engineering_infrastructure import \
#     EngineeringInfrastructure
# from server.apps.investment_site.models.investment_site import \
#     InvestmentSite
# from server.apps.investment_site.models.subway_station import SubwayStation
# from server.apps.investment_site.services.parsing.investment_object_type import \
#     parsing_technopolis
#
# FUNCTION_MAP: Dict[int, Any] = {
#     2: parsing_technopolis,
# }
#
#
# def parsing_investment_site():
#     response = requests.post(
#         url=(
#             'https://api.investmoscow.ru/investmoscow/investment-map/'
#             'v1/InvestmentSite/searchInvestmentObjects'
#         ),
#         headers={'Content-Type': 'application/json'},
#         json={
#             'PageNumber': 1,
#             'PageSize': 500,
#             'districts': [],
#             'metros': [],
#         }
#     )
#     for entity in response.json()['entities']:
#         investment_site, created = InvestmentSite.objects.get_or_create(
#             investment_site_id=entity.get('InvestmentSiteId'),
#             defaults={
#                 'main_photo_url': entity.get('previewImgUrl'),
#                 'name': entity.get('name'),
#                 'longitude': entity.get('coords').get('coordinates')[0],
#                 'latitude': entity.get('coords').get('coordinates')[1],
#                 'investment_object_type': entity.get('type'),
#             },
#         )
#         extra_data, created = ExtraData.objects.get_or_create(
#             investment_site=investment_site,
#             defaults={
#                 'address': entity.get('address'),
#                 'area': entity.get('area'),
#                 'details_url': entity.get('detailsUrl'),
#                 'district_id': entity.get('districtId'),
#                 'district_name': entity.get('districtName'),
#                 'region_id': entity.get('regionId'),
#                 'region_name': entity.get('regionName'),
#             }
#         )
#         for response_subway_station in entity.get('subwayStations'):
#             subway_station, created = SubwayStation.objects.get_or_create(
#                 subway_station_id=response_subway_station.get('subwayStationId'),  # noqa: E501
#                 defaults={
#                     'subway_station_name':
#                         response_subway_station.get('subwayStationName'),
#                 },
#             )
#             extra_data.subway_stations.add(subway_station)
#
#         FUNCTION_MAP.get(entity.get('type'))(
#             investment_site=investment_site,
#             extra_data=extra_data,
#         )
