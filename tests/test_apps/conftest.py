from typing import Callable, Any, Tuple, Dict

import factory
import pytest
from factory import LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from pytest_factoryboy import register
from rest_framework.fields import DateTimeField
from rest_framework.response import Response
from rest_framework.test import APIClient

from server.apps.investment_object.models import InvestmentObject, \
    EconomicActivity, TransactionForm, Restriction, Privilege, RealEstate, \
    Infrastructure, ReadyBusiness, SpecializedSite, TenderLot
from server.apps.personal_cabinet.models import Subscription, \
    TerritorialLocation, SelectionRequest, SubSector, Sector, Message, Business
from server.apps.service_interaction.models import Event, Topic, Comment, Post
from server.apps.services.enums import TransactionFormType, ObjectType, \
    InfrastructureAvailability, SubscriptionType
from server.apps.support.models import ProblemSubcategory, ServiceSupport, \
    ProblemCategory, ProblemTheme, Problem
from server.apps.user.models import User

fake = Faker()


def lazy(method: Callable, *args, **kwargs) -> Any:
    """Обертка для метода, чтобы вызывать его lazy."""
    return LazyAttribute(lambda argument: method(*args, **kwargs))


def random_text_choice(choice_source) -> LazyAttribute:
    """Случайный вариант из choice_source (например TextChoices)."""
    return LazyAttribute(
        lambda argument: fake.random.choice(choice_source.choices)[0],
    )


def response_without_keys(
    response_json: Dict[str, Any],
    keys: Tuple[str, ...] = ('permission_rules',),
) -> Dict[str, Any]:
    """Response без permissionRules."""
    for key in keys:
        response_json.pop(key)
    return response_json


class UserFactory(DjangoModelFactory):
    """Фабрика для User."""

    last_login = lazy(fake.date_time_this_year)
    is_superuser = False
    username = lazy(fake.word)
    first_name = lazy(fake.first_name)
    last_name = lazy(fake.last_name)
    middle_name = lazy(fake.prefix)
    is_active = True
    date_joined = factory.LazyAttribute(
        lambda user: fake.date_time_this_month(),
    )
    email = lazy(fake.email)
    can_change_password = True
    phone = lazy(fake.phone_number)


    class Meta:
        model = User


class EconomicActivityFactory(DjangoModelFactory):
    """Фабрика для EconomicActivity."""

    code = lazy(fake.paragraph)
    parent_code = lazy(fake.paragraph)
    section = lazy(fake.paragraph)
    name = lazy(fake.paragraph)
    comment = lazy(fake.paragraph)

    class Meta:
        model = EconomicActivity


class TransactionFormFactory(DjangoModelFactory):
    """Фабрика для TransactionForm."""

    name = lazy(fake.paragraph)
    transaction_form_type = random_text_choice(TransactionFormType)

    class Meta:
        model = TransactionForm


class RestrictionFactory(DjangoModelFactory):
    """Фабрика для Restriction."""

    name = lazy(fake.paragraph)

    class Meta:
        model = Restriction


class PrivilegeFactory(DjangoModelFactory):
    """Фабрика для Privilege."""

    name = lazy(fake.paragraph)


    class Meta:
        model = Privilege


class InfrastructureFactory(DjangoModelFactory):
    """Фабрика для Infrastructure."""

    name = lazy(fake.paragraph)
    consumption_tariff = lazy(fake.paragraph)
    transportation_tariff = lazy(fake.paragraph)
    max_allowable_power = lazy(fake.paragraph)
    free_power = lazy(fake.paragraph)
    throughput = lazy(fake.paragraph)
    other_characteristics = lazy(fake.paragraph)
    availability =  random_text_choice(InfrastructureAvailability)

    class Meta:
        model = Infrastructure


class InvestmentObjectFactory(DjangoModelFactory):
    """Фабрика для InvestmentObject."""

    name = lazy(fake.paragraph)
    main_photo_url = lazy(fake.paragraph)
    object_type = random_text_choice(ObjectType)
    transaction_form = factory.SubFactory(TransactionFormFactory)
    cost = lazy(fake.pyfloat)
    land_area = lazy(fake.pyfloat)
    building_area = lazy(fake.pyfloat)
    location = lazy(fake.paragraph)
    url = lazy(fake.paragraph)
    data_source = lazy(fake.paragraph)
    longitude = lazy(fake.pydecimal, 3, 3)
    latitude = lazy(fake.pydecimal, 3, 3)

    class Meta:
        model = InvestmentObject


class RealEstateFactory(DjangoModelFactory):
    """Фабрика для RealEstate."""

    investment_object = factory.SubFactory(InvestmentObjectFactory)
    external_id = lazy(fake.paragraph)
    preferential_treatment = lazy(fake.paragraph)
    preferential_treatment_object_code = lazy(fake.paragraph)
    preferential_treatment_object_name = lazy(fake.paragraph)
    support_infrastructure_object = lazy(fake.paragraph)
    support_infrastructure_object_code = lazy(fake.paragraph)
    support_infrastructure_object_name = lazy(fake.paragraph)
    region = lazy(fake.paragraph)
    address = lazy(fake.paragraph)
    nearest_cities = lazy(fake.paragraph)
    site_format = lazy(fake.paragraph)
    site_type = lazy(fake.paragraph)
    ownership_type = lazy(fake.paragraph)
    rental_period = lazy(fake.paragraph)
    procedure_determining_cost = lazy(fake.paragraph)
    hazard_class_object = lazy(fake.paragraph)
    characteristic_object = lazy(fake.paragraph)
    land_cadastral_number = lazy(fake.paragraph)
    permitted_use_options = lazy(fake.paragraph)
    cupping = lazy(fake.paragraph)
    land_category = lazy(fake.paragraph)
    building_cadastral_number = lazy(fake.paragraph)
    building_technical_specifications = lazy(fake.paragraph)
    owner_name = lazy(fake.paragraph)
    owner_inn = lazy(fake.paragraph)
    other_characteristics = lazy(fake.paragraph)
    application_procedure = lazy(fake.paragraph)
    documents_for_application = lazy(fake.paragraph)
    application_form_url = lazy(fake.paragraph)
    urban_planning = lazy(fake.paragraph)
    other_information = lazy(fake.paragraph)
    maip = lazy(fake.paragraph)
    benefit_description = lazy(fake.paragraph)

    class Meta:
        model = RealEstate


class ReadyBusinessFactory(DjangoModelFactory):
    """Фабрика для ReadyBusiness."""

    investment_object = factory.SubFactory(InvestmentObjectFactory)
    external_id = lazy(fake.paragraph)
    description = lazy(fake.paragraph)

    class Meta:
        model = ReadyBusiness


class SpecializedSiteFactory(DjangoModelFactory):
    """Фабрика для SpecializedSite."""

    investment_object = factory.SubFactory(InvestmentObjectFactory)
    external_id = lazy(fake.paragraph)
    sez = lazy(fake.paragraph)
    tad = lazy(fake.paragraph)
    region = lazy(fake.paragraph)
    nearest_cities = lazy(fake.paragraph)
    number_residents = lazy(fake.pyint)
    document_url = lazy(fake.paragraph)
    year_formation = lazy(fake.pyint)
    validity = lazy(fake.pyint)
    additional_services = lazy(fake.paragraph)
    object_administrator_name = lazy(fake.paragraph)
    address = lazy(fake.paragraph)
    working_hours = lazy(fake.paragraph)
    income_tax = lazy(fake.paragraph)
    property_tax = lazy(fake.paragraph)
    land_tax = lazy(fake.paragraph)
    transport_tax = lazy(fake.paragraph)
    insurance_premiums = lazy(fake.paragraph)
    is_free_customs_zone_regime = lazy(fake.paragraph)
    resident_info = lazy(fake.paragraph)
    minimum_investment_amount = lazy(fake.paragraph)
    urban_planning = lazy(fake.paragraph)

    class Meta:
        model = SpecializedSite


class TenderLotFactory(DjangoModelFactory):
    """Фабрика для TenderLot."""

    investment_object = factory.SubFactory(InvestmentObjectFactory)
    external_id = lazy(fake.paragraph)
    description = lazy(fake.paragraph)

    class Meta:
        model = TenderLot


class ServiceSupportFactory(DjangoModelFactory):
    """Фабрика для ServiceSupport."""


    external_id = lazy(fake.paragraph)
    region = lazy(fake.paragraph)
    service_support_type = lazy(fake.paragraph)
    name = lazy(fake.paragraph)
    support_type = lazy(fake.paragraph)
    support_level = lazy(fake.paragraph)
    description = lazy(fake.paragraph)
    legal_act = lazy(fake.paragraph)
    url_legal_act = lazy(fake.paragraph)
    url_application_form = lazy(fake.paragraph)
    name_responsible_body = lazy(fake.paragraph)
    economic_activities = factory.SubFactory(EconomicActivityFactory)
    restrictions = factory.SubFactory(RestrictionFactory)
    msp_roster = lazy(fake.paragraph)
    msp_roster = lazy(fake.paragraph)
    applicant_requirement = lazy(fake.paragraph)
    applicant_procedure = lazy(fake.paragraph)
    required_document = lazy(fake.paragraph)
    url = lazy(fake.paragraph)

    class Meta:
        model = ServiceSupport


class ProblemCategoryFactory(DjangoModelFactory):
    """Фабрика для ProblemCategory."""

    external_id = lazy(fake.paragraph)
    name = lazy(fake.paragraph)

    class Meta:
        model = ProblemCategory


class ProblemSubcategoryFactory(DjangoModelFactory):
    """Фабрика для ProblemSubcategory."""


    problem_category = factory.SubFactory(ProblemCategoryFactory)
    external_id = lazy(fake.paragraph)
    name = lazy(fake.paragraph)


    class Meta:
        model = ProblemSubcategory


class ProblemThemeFactory(DjangoModelFactory):
    """Фабрика для ProblemTheme."""

    problem_subcategory = factory.SubFactory(ProblemSubcategoryFactory)
    external_id = lazy(fake.paragraph)
    name = lazy(fake.paragraph)

    class Meta:
        model = ProblemTheme


class ProblemFactory(DjangoModelFactory):
    """Фабрика для Problem."""


    problem_theme = factory.SubFactory(ProblemThemeFactory)
    external_id = lazy(fake.paragraph)
    name = lazy(fake.paragraph)
    additional_info = lazy(fake.paragraph)
    url = lazy(fake.paragraph)


    class Meta:
        model = Problem


class EventFactory(DjangoModelFactory):
    """Фабрика для Event."""

    photo = lazy(fake.file_name)
    name = lazy(fake.paragraph)
    event_datetime = lazy(fake.date_time_this_month)
    shot_description = lazy(fake.paragraph)
    description = lazy(fake.paragraph)
    event_type = lazy(fake.paragraph)

    class Meta:
        model = Event


class TopicFactory(DjangoModelFactory):
    """Фабрика для Topic."""

    name = lazy(fake.paragraph)
    shot_description = lazy(fake.paragraph)
    description = lazy(fake.paragraph)

    class Meta:
        model = Topic


class CommentFactory(DjangoModelFactory):
    """Фабрика для Comment."""

    user = factory.SubFactory(UserFactory)
    text = lazy(fake.paragraph)
    content_object = factory.SubFactory(InvestmentObjectFactory)

    class Meta:
        model = Comment


class PostFactory(DjangoModelFactory):
    """Фабрика для Post."""

    user = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    text = lazy(fake.paragraph)

    class Meta:
        model = Post


class TerritorialLocationFactory(DjangoModelFactory):
    """Фабрика для TerritorialLocation."""

    short_name = lazy(fake.paragraph)
    full_name = lazy(fake.paragraph)

    class Meta:
        model = TerritorialLocation


class SelectionRequestFactory(DjangoModelFactory):
    """Фабрика для SelectionRequest."""

    user = factory.SubFactory(UserFactory)
    anonymous_user_id = lazy(fake.paragraph)
    is_actual = lazy(fake.pybool)
    is_bot_response_waiting = lazy(fake.pybool)

    class Meta:
        model = SelectionRequest


class SubSectorFactory(DjangoModelFactory):
    """Фабрика для SubSector."""

    name = lazy(fake.paragraph)

    class Meta:
        model = SubSector


class SectorFactory(DjangoModelFactory):
    """Фабрика для Sector."""

    name = lazy(fake.paragraph)

    class Meta:
        model = Sector


class MessageFactory(DjangoModelFactory):
    """Фабрика для Message."""

    owner_type = lazy(fake.paragraph)
    selection_request = factory.SubFactory(SelectionRequestFactory)
    text = lazy(fake.paragraph)

    class Meta:
        model = Message


class SubscriptionFactory(DjangoModelFactory):
    """Фабрика для Subscription."""

    user = factory.SubFactory(UserFactory)
    subscription_type = random_text_choice(SubscriptionType)
    topics = factory.SubFactory(TopicFactory)
    email = lazy(fake.ascii_free_email)
    telegram_username = lazy(fake.word)

    class Meta:
        model = Subscription


class BusinessFactory(DjangoModelFactory):
    """Фабрика для Business."""

    user = factory.SubFactory(UserFactory)
    position = lazy(fake.paragraph)
    business_type = lazy(fake.paragraph)
    inn = lazy(fake.paragraph)
    sector = factory.SubFactory(SectorFactory)
    sub_sector = factory.SubFactory(SubSectorFactory)
    territorial_location = factory.SubFactory(TerritorialLocationFactory)
    hid = lazy(fake.paragraph)
    short_business_name = lazy(fake.paragraph)
    full_business_name = lazy(fake.paragraph)
    management_name = lazy(fake.paragraph)
    management_position = lazy(fake.paragraph)
    full_opf = lazy(fake.paragraph)
    short_opf = lazy(fake.paragraph)
    okved_code = lazy(fake.paragraph)
    first_name = lazy(fake.paragraph)
    last_name = lazy(fake.paragraph)
    middle_name = lazy(fake.paragraph)
    address = lazy(fake.paragraph)
    country = lazy(fake.paragraph)
    region = lazy(fake.paragraph)
    city_area = lazy(fake.paragraph)
    city_district = lazy(fake.paragraph)
    phone = lazy(fake.paragraph)
    email = lazy(fake.ascii_free_email)
    site = lazy(fake.paragraph)
    tax_system_type = lazy(fake.paragraph)
    economic_activities = factory.SubFactory(EconomicActivityFactory)

    class Meta:
        model = Business


register(InvestmentObjectFactory)
register(InfrastructureFactory)
register(TenderLotFactory)
register(EconomicActivityFactory)
register(SpecializedSiteFactory)
register(TransactionFormFactory)
register(PrivilegeFactory)
register(RestrictionFactory)
register(ReadyBusinessFactory)
register(RealEstateFactory)
register(ProblemThemeFactory)
register(ProblemFactory)
register(ServiceSupportFactory)
register(ProblemCategoryFactory)
register(ProblemSubcategoryFactory)
register(PostFactory)
register(CommentFactory)
register(TopicFactory)
register(EventFactory)
register(MessageFactory)
register(SectorFactory)
register(SubSectorFactory)
register(SelectionRequestFactory)
register(BusinessFactory)
register(TerritorialLocationFactory)
register(SubscriptionFactory)
register(UserFactory)


@pytest.fixture
def transaction_form_format():
    """Формат TransactionForm."""
    def _transaction_form_format(transaction_form: TransactionForm):
        return {
            'id': transaction_form.id,
            'name': transaction_form.name,
            'transaction_form_type': transaction_form.transaction_form_type,
            'transaction_form_type_label':
                transaction_form.get_transaction_form_type_display(),
            'created_at':
                DateTimeField().to_representation(transaction_form.created_at),
            'updated_at':
                DateTimeField().to_representation(transaction_form.updated_at),
        }
    return _transaction_form_format


@pytest.fixture
def investment_object_format(transaction_form_format):
    """Формат InvestmentObject."""
    def _investment_object_format(investment_object):
        return {
            'id': investment_object.id,
            'name': investment_object.name,
            'main_photo_url': investment_object.main_photo_url,
            'photo_urls': investment_object.photo_urls,
            'object_type': investment_object.object_type,
            'economic_activities': [],
            'transaction_form': transaction_form_format(
                investment_object.transaction_form
            ),
            'cost': investment_object.cost,
            'land_area': investment_object.land_area,
            'building_area': investment_object.building_area,
            'location': investment_object.location,
            'url': investment_object.url,
            'data_source': investment_object.data_source,
            'longitude': str(investment_object.longitude),
            'latitude': str(investment_object.latitude),

            'tender_lot': None,
            'real_estate': None,
            'specialized_site': None,
            'ready_business': None,
            'content_type_id': investment_object.content_type_id,
            'created_at':
                DateTimeField().to_representation(investment_object.created_at),
            'updated_at':
                DateTimeField().to_representation(investment_object.updated_at),
        }
    return _investment_object_format


@pytest.fixture
def real_estate_format():
    """Формат RealEstate."""
    def _real_estate_format(real_estate):
        return {
            'id': real_estate.id,
            'investment_object': real_estate.investment_object.id,
            'external_id': real_estate.external_id,
            'preferential_treatment': real_estate.preferential_treatment,
            'preferential_treatment_object_code':
                real_estate.preferential_treatment_object_code,
            'preferential_treatment_object_name':
                real_estate.preferential_treatment_object_name,
            'support_infrastructure_object':
                real_estate.support_infrastructure_object,
            'support_infrastructure_object_code':
                real_estate.support_infrastructure_object_code,
            'support_infrastructure_object_name':
                real_estate.support_infrastructure_object_name,
            'region': real_estate.region,
            'address': real_estate.address,
            'nearest_cities': real_estate.nearest_cities,
            'site_format': real_estate.site_format,
            'site_type': real_estate.site_type,
            'ownership_type': real_estate.ownership_type,
            'rental_period': real_estate.rental_period,
            'procedure_determining_cost': real_estate.procedure_determining_cost,
            'hazard_class_object': real_estate.hazard_class_object,
            'characteristic_object': real_estate.characteristic_object,
            'land_cadastral_number': real_estate.land_cadastral_number,
            'permitted_use_options': real_estate.permitted_use_options,
            'cupping': real_estate.cupping,
            'land_category': real_estate.land_category,
            'building_cadastral_number':
                real_estate.building_cadastral_number,
            'building_technical_specifications':
                real_estate.building_technical_specifications,
            'owner_name': real_estate.owner_name,
            'owner_inn': real_estate.owner_inn,
            'other_characteristics': real_estate.other_characteristics,
            'application_procedure': real_estate.application_procedure,
            'documents_for_application': real_estate.documents_for_application,
            'application_form_url': real_estate.application_form_url,
            'urban_planning': real_estate.urban_planning,
            'other_information': real_estate.other_information,
            'maip': real_estate.maip,
            'benefit_description': real_estate.benefit_description,
            'infrastructures': [],
            'created_at':
                DateTimeField().to_representation(real_estate.created_at),
            'updated_at':
                DateTimeField().to_representation(real_estate.updated_at),
        }
    return _real_estate_format


@pytest.fixture
def ready_business_format():
    """Формат ReadyBusiness."""
    def _ready_business_format(ready_business):
        return {
            'id': ready_business.id,
            'investment_object': ready_business.investment_object.id,
            'external_id': ready_business.external_id,
            'description': ready_business.description,
            'extra_data': ready_business.extra_data,
            'created_at':
                DateTimeField().to_representation(ready_business.created_at),
            'updated_at':
                DateTimeField().to_representation(ready_business.updated_at),
        }
    return _ready_business_format


@pytest.fixture
def restriction_format():
    """Формат Restriction."""
    def _restriction_format(restriction: Restriction):
        return {
            'id': restriction.id,
            'name': restriction.name,
            'created_at':
                DateTimeField().to_representation(restriction.created_at),
            'updated_at':
                DateTimeField().to_representation(restriction.updated_at),
        }
    return _restriction_format


@pytest.fixture
def privilege_format():
    """Формат Privilege."""
    def _privilege_format(privilege: Privilege):
        return {
            'id': privilege.id,
            'name': privilege.name,
            'created_at':
                DateTimeField().to_representation(privilege.created_at),
            'updated_at':
                DateTimeField().to_representation(privilege.updated_at),
        }
    return _privilege_format


@pytest.fixture
def transaction_form_format():
    """Формат TransactionForm."""
    def _transaction_form_format(transaction_form: TransactionForm):
        return {
            'id': transaction_form.id,
            'name': transaction_form.name,
            'transaction_form_type': transaction_form.transaction_form_type,
            'created_at':
                DateTimeField().to_representation(transaction_form.created_at),
            'updated_at':
                DateTimeField().to_representation(transaction_form.updated_at),
        }
    return _transaction_form_format


@pytest.fixture
def specialized_site_format():
    """Формат SpecializedSite."""
    def _specialized_site_format(specialized_site):
        return {
            'id': specialized_site.id,
            'investment_object': specialized_site.investment_object.id,
            'external_id': specialized_site.external_id,
            'sez': specialized_site.sez,
            'tad': specialized_site.tad,
            'region': specialized_site.region,
            'nearest_cities': specialized_site.nearest_cities,
            'number_residents': specialized_site.number_residents,
            'document_url': specialized_site.document_url,
            'year_formation': specialized_site.year_formation,
            'validity': specialized_site.validity,
            'restrictions': [],
            'infrastructures': [],
            'additional_services': specialized_site.additional_services,
            'object_administrator_name': specialized_site.object_administrator_name,
            'address': specialized_site.address,
            'working_hours': specialized_site.working_hours,
            'income_tax': specialized_site.income_tax,
            'property_tax': specialized_site.property_tax,
            'land_tax': specialized_site.land_tax,
            'transport_tax': specialized_site.transport_tax,
            'insurance_premiums': specialized_site.insurance_premiums,
            'privileges': [],
            'is_free_customs_zone_regime': specialized_site.is_free_customs_zone_regime,
            'resident_info': specialized_site.resident_info,
            'minimum_investment_amount': specialized_site.minimum_investment_amount,
            'urban_planning': specialized_site.urban_planning,
            'created_at':
                DateTimeField().to_representation(specialized_site.created_at),
            'updated_at':
                DateTimeField().to_representation(specialized_site.updated_at),
        }
    return _specialized_site_format


@pytest.fixture
def economic_activity_format():
    """Формат EconomicActivity."""
    def _economic_activity_format(economic_activity):
        return {
            'id': economic_activity.id,
            'code': economic_activity.code,
            'parent_code': economic_activity.parent_code,
            'section': economic_activity.section,
            'name': economic_activity.name,
            'comment': economic_activity.comment,
            'created_at':
                DateTimeField().to_representation(economic_activity.created_at),
            'updated_at':
                DateTimeField().to_representation(economic_activity.updated_at),
        }
    return _economic_activity_format


@pytest.fixture
def tender_lot_format():
    """Формат TenderLot."""
    def _tender_lot_format(tender_lot: TenderLot):
        return {
            'id': tender_lot.id,
            'investment_object': tender_lot.investment_object.id,
            'external_id': tender_lot.external_id,
            'description': tender_lot.description,
            'extra_data': tender_lot.extra_data,
            'created_at':
                DateTimeField().to_representation(tender_lot.created_at),
            'updated_at':
                DateTimeField().to_representation(tender_lot.updated_at),
        }
    return _tender_lot_format


@pytest.fixture
def infrastructure_format():
    """Формат Infrastructure."""
    def _infrastructure_format(infrastructure):
        return {
            'id': infrastructure.id,
            'name': infrastructure.name,
            'consumption_tariff': infrastructure.consumption_tariff,
            'transportation_tariff': infrastructure.transportation_tariff,
            'max_allowable_power': infrastructure.max_allowable_power,
            'free_power': infrastructure.free_power,
            'throughput': infrastructure.throughput,
            'other_characteristics': infrastructure.other_characteristics,
            'availability': infrastructure.availability,
            'availability_label': infrastructure.get_availability_display(),
            'created_at':
                DateTimeField().to_representation(infrastructure.created_at),
            'updated_at':
                DateTimeField().to_representation(infrastructure.updated_at),
        }
    return _infrastructure_format


@pytest.fixture
def problem_subcategory_format():
    """Формат ProblemSubcategory."""
    def _problem_subcategory_format(problem_subcategory: ProblemSubcategory):
        return {
            'id': problem_subcategory.id,
            'problem_category': problem_subcategory.problem_category,
            'external_id': problem_subcategory.external_id,
            'name': problem_subcategory.name,
        }
    return _problem_subcategory_format



@pytest.fixture
def subscription_format():
    """Формат Subscription."""
    def _subscription_format(subscription: Subscription):
        return {
            'id': subscription.id,
            'user': subscription.user,
            'subscription_type': subscription.subscription_type,
            'topics': subscription.topics,
            'email': subscription.email,
            'telegram_username': subscription.telegram_username,
        }
    return _subscription_format


@pytest.fixture
def territorial_location_format():
    """Формат TerritorialLocation."""
    def _territorial_location_format(territorial_location: TerritorialLocation):
        return {
            'id': territorial_location.id,
            'short_name': territorial_location.short_name,
            'full_name': territorial_location.full_name,
        }
    return _territorial_location_format


@pytest.fixture
def business_format():
    """Формат Business."""
    def _business_format(business):
        return {
            'id': business.id,
            'user': business.user,
            'position': business.position,
            'business_type': business.business_type,
            'inn': business.inn,
            'sector': business.sector,
            'sub_sector': business.sub_sector,
            'territorial_location': business.territorial_location,
            'hid': business.hid,
            'short_business_name': business.short_business_name,
            'full_business_name': business.full_business_name,
            'management_name': business.management_name,
            'management_position': business.management_position,
            'full_opf': business.full_opf,
            'short_opf': business.short_opf,
            'okved_code': business.okved_code,
            'first_name': business.first_name,
            'last_name': business.last_name,
            'middle_name': business.middle_name,
            'address': business.address,
            'country': business.country,
            'region': business.region,
            'city_area': business.city_area,
            'city_district': business.city_district,
            'phone': business.phone,
            'email': business.email,
            'site': business.site,
            'tax_system_type': business.tax_system_type,
            'economic_activities': business.economic_activities,
        }
    return _business_format


@pytest.fixture
def selection_request_format():
    """Формат SelectionRequest."""
    def _selection_request_format(selection_request: SelectionRequest):
        return {
            'id': selection_request.id,
            'user': selection_request.user,
            'anonymous_user_id': selection_request.anonymous_user_id,
            'is_actual': selection_request.is_actual,
            'is_bot_response_waiting': selection_request.is_bot_response_waiting,
        }
    return _selection_request_format


@pytest.fixture
def sub_sector_format():
    """Формат SubSector."""
    def _sub_sector_format(sub_sector: SubSector):
        return {
            'id': sub_sector.id,
            'name': sub_sector.name,
        }
    return _sub_sector_format


@pytest.fixture
def sector_format():
    """Формат Sector."""
    def _sector_format(sector: Sector):
        return {
            'id': sector.id,
            'name': sector.name,
        }
    return _sector_format


@pytest.fixture
def message_format():
    """Формат Message."""
    def _message_format(message: Message):
        return {
            'id': message.id,
            'owner_type': message.owner_type,
            'selection_request': message.selection_request,
            'text': message.text,
            'parent': message.parent,
        }
    return _message_format


@pytest.fixture
def event_format():
    """Формат Event."""
    def _event_format(event):
        return {
            'id': event.id,
            'photo': event.photo,
            'name': event.name,
            'event_datetime': event.event_datetime,
            'shot_description': event.shot_description,
            'description': event.description,
            'event_type': event.event_type,
        }
    return _event_format


@pytest.fixture
def topic_format():
    """Формат Topic."""
    def _topic_format(topic: Topic):
        return {
            'id': topic.id,
            'name': topic.name,
            'shot_description': topic.shot_description,
            'description': topic.description,
        }
    return _topic_format


@pytest.fixture
def comment_format():
    """Формат Comment."""
    def _comment_format(comment: Comment):
        return {
            'id': comment.id,
            'user': comment.user,
            'text': comment.text,
            'content_type': comment.content_type,
            'object_id': comment.object_id,
        }
    return _comment_format


@pytest.fixture
def post_format():
    """Формат Post."""
    def _post_format(post: Post):
        return {
            'id': post.id,
            'user': post.user,
            'topic': post.topic,
            'parent': post.parent,
            'text': post.text,
        }
    return _post_format



@pytest.fixture
def problem_subcategory_format():
    """Формат ProblemSubcategory."""
    def _problem_subcategory_format(problem_subcategory: ProblemSubcategory):
        return {
            'id': problem_subcategory.id,
            'problem_category': problem_subcategory.problem_category,
            'external_id': problem_subcategory.external_id,
            'name': problem_subcategory.name,
        }
    return _problem_subcategory_format


@pytest.fixture
def problem_category_format():
    """Формат ProblemCategory."""
    def _problem_category_format(problem_category: ProblemCategory):
        return {
            'id': problem_category.id,
            'external_id': problem_category.external_id,
            'name': problem_category.name,
        }
    return _problem_category_format


@pytest.fixture
def service_support_format():
    """Формат ServiceSupport."""
    def _service_support_format(service_support):
        return {
            'id': service_support.id,
            'external_id': service_support.external_id,
            'region': service_support.region,
            'service_support_type': service_support.service_support_type,
            'name': service_support.name,
            'support_type': service_support.support_type,
            'support_level': service_support.support_level,
            'description': service_support.description,
            'legal_act': service_support.legal_act,
            'url_legal_act': service_support.url_legal_act,
            'url_application_form': service_support.url_application_form,
            'name_responsible_body': service_support.name_responsible_body,
            'economic_activities': service_support.economic_activities,
            'restrictions': service_support.restrictions,
            'msp_roster': service_support.msp_roster,
            'applicant_requirement': service_support.applicant_requirement,
            'applicant_procedure': service_support.applicant_procedure,
            'required_document': service_support.required_document,
            'url': service_support.url,
        }
    return _service_support_format


@pytest.fixture
def problem_format():
    """Формат Problem."""
    def _problem_format(problem):
        return {
            'id': problem.id,
            'problem_theme': problem.problem_theme,
            'external_id': problem.external_id,
            'name': problem.name,
            'additional_info': problem.additional_info,
            'url': problem.url,
        }
    return _problem_format


@pytest.fixture
def problem_theme_format():
    """Формат ProblemTheme."""
    def _problem_theme_format(problem_theme: ProblemTheme):
        return {
            'id': problem_theme.id,
            'problem_subcategory': problem_theme.problem_subcategory,
            'external_id': problem_theme.external_id,
            'name': problem_theme.name,
        }
    return _problem_theme_format
