from rest_framework import serializers

from server.apps.investment_object.models import (
    EconomicActivity,
    InvestmentObject,
    Privilege,
    ReadyBusiness,
    RealEstate,
    Restriction,
    SpecializedSite,
    TenderLot,
)


class BaseEconomicActivitySerializer(serializers.ModelSerializer):
    """Базовый сериалайзер экономической деятельности."""

    class Meta:
        model = EconomicActivity
        fields = (
            'id',
            'code',
            'name',
        )


class BaseInfrastructureSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер инфраструктуры."""

    class Meta:
        model = EconomicActivity
        fields = (
            'id',
            'name',
            'consumption_tariff',
            'transportation_tariff',
            'max_allowable_power',
            'free_power',
            'throughput',
            'other_characteristics',
            'availability',
        )


class BaseInvestmentObjectSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер инвестиционных площадок."""

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'external_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'object_type',
            'url',
            'extra_data',
            'longitude',
            'latitude',
        )


class BasePrivilegeSerializer(serializers.ModelSerializer):
    """Сериалайзер льгот."""

    class Meta:
        model = Privilege
        fields = (
            'id',
            'name',
        )


class BaseReadyBusinessSerializer(serializers.ModelSerializer):
    """Сериалайзер готового бизнеса."""

    class Meta:
        model = ReadyBusiness
        fields = (
            'id',
            'external_id',
            'name',
            'description',
            'extra_data',
        )


class BaseRestrictionSerializer(serializers.ModelSerializer):
    """Сериалайзер ограничений по видам деятельности."""

    class Meta:
        model = Restriction
        fields = (
            'id',
            'name',
        )


class BaseRealEstateSerializer(serializers.ModelSerializer):
    """Сериалайзер недвижимости."""

    economic_activities = BaseEconomicActivitySerializer(many=True)
    infrastructures = BaseInfrastructureSerializer(many=True)

    class Meta:
        model = RealEstate
        fields = (
            'id',
            'investment_object',
            'preferential_treatment',
            'preferential_treatment_object_code',
            'preferential_treatment_object_name',
            'support_infrastructure_object',
            'support_infrastructure_object_code',
            'support_infrastructure_object_name',
            'region',
            'municipality',
            'address',
            'nearest_cities',
            'site_format',
            'site_type',
            'ownership_type',
            'transaction_form',
            'object_cost',
            'rental_period',
            'procedure_determining_cost',
            'hazard_class_object',
            'characteristic_object',
            'land_free_area',
            'land_cadastral_number',
            'permitted_use_options',
            'is_cupping',
            'land_category',
            'building_free_area',
            'building_cadastral_number',
            'building_technical_specifications',
            'owner_name',
            'owner_inn',
            'owner_website',
            'other_characteristics',
            'application_procedure',
            'documents_for_application',
            'application_form_url',
            'urban_planning',
            'other_information',
            'is_maip',
            'benefit_description',
            'longitude',
            'latitude',
            'economic_activities',
            'infrastructures',
        )


class BaseTenderLotSerializer(serializers.ModelSerializer):
    """Сериалайзер лота тендера."""

    class Meta:
        model = TenderLot
        fields = (
            'id',
            'tender_lot_id',
            'name',
            'description',
            'extra_data',
            'url',
        )


class BaseSpecializedSiteSerializer(serializers.ModelSerializer):
    """Сериалайзер ограничений по видам деятельности."""

    economic_activities = BaseEconomicActivitySerializer(many=True)
    restrictions = BaseRestrictionSerializer(many=True)
    infrastructures = BaseInfrastructureSerializer(many=True)
    privileges = BasePrivilegeSerializer(many=True)

    class Meta:
        model = SpecializedSite
        fields = (
            'id',
            'investment_object',
            'sez',
            'tad',
            'name',
            'region',
            'municipality',
            'nearest_cities',
            'number_residents',
            'document_url',
            'year_formation',
            'validity',
            'minimum_rental_price',
            'total_area',
            'is_possibility_redemption',
            'economic_activities',
            'restrictions',
            'infrastructures',
            'additional_services',
            'object_administrator_name',
            'address',
            'website',
            'working_hours',
            'income_tax',
            'property_tax',
            'land_tax',
            'transport_tax',
            'insurance_premiums',
            'privileges',
            'is_free_customs_zone_regime',
            'resident_info',
            'minimum_investment_amount',
            'urban_planning',
            'longitude',
            'latitude',
        )

