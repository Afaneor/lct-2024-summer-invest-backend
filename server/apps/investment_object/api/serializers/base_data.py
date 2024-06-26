from rest_framework import serializers

from server.apps.investment_object.models import (
    EconomicActivity,
    Infrastructure,
    InvestmentObject,
    Privilege,
    ReadyBusiness,
    RealEstate,
    Restriction,
    SpecializedSite,
    TenderLot,
    TransactionForm,
)


class BaseTransactionFormSerializer(serializers.ModelSerializer):
    """Сериалайзер формы транзакции."""

    transaction_form_type_label = serializers.SerializerMethodField()

    class Meta:
        model = TransactionForm
        fields = (
            'id',
            'name',
            'transaction_form_type',
            'transaction_form_type_label',
        )

    def get_transaction_form_type_label(
        self,
        transaction_form: TransactionForm,
    ):
        """Подпись к transaction_form_type."""
        return transaction_form.get_transaction_form_type_display()


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

    availability_label = serializers.SerializerMethodField()

    class Meta:
        model = Infrastructure
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
            'availability_label',
        )

    def get_availability_label(
        self,
        infrastructure: Infrastructure,
    ):
        """Подпись к availability."""
        return infrastructure.get_availability_display()


class BaseInvestmentObjectSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер инвестиционных площадок."""

    object_type_label = serializers.SerializerMethodField()

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'external_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'object_type',
            'object_type_label',
            'url',
            'extra_data',
            'longitude',
            'latitude',
        )

    def get_object_type_label(
        self,
        investment_object: InvestmentObject,
    ):
        """Подпись к object_type."""
        return investment_object.get_object_type_display()


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
            'investment_object',
            'external_id',
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

    infrastructures = BaseInfrastructureSerializer(many=True)

    class Meta:
        model = RealEstate
        fields = (
            'id',
            'investment_object',
            'external_id',
            'preferential_treatment',
            'preferential_treatment_object_code',
            'preferential_treatment_object_name',
            'support_infrastructure_object',
            'support_infrastructure_object_code',
            'support_infrastructure_object_name',
            'region',
            'address',
            'nearest_cities',
            'site_format',
            'site_type',
            'ownership_type',
            'rental_period',
            'procedure_determining_cost',
            'hazard_class_object',
            'characteristic_object',
            'land_cadastral_number',
            'permitted_use_options',
            'cupping',
            'land_category',
            'building_cadastral_number',
            'building_technical_specifications',
            'owner_name',
            'owner_inn',
            'other_characteristics',
            'application_procedure',
            'documents_for_application',
            'application_form_url',
            'urban_planning',
            'other_information',
            'maip',
            'benefit_description',
            'infrastructures',
        )


class BaseTenderLotSerializer(serializers.ModelSerializer):
    """Сериалайзер лота тендера."""

    class Meta:
        model = TenderLot
        fields = (
            'id',
            'investment_object',
            'external_id',
            'description',
            'extra_data',
        )


class BaseSpecializedSiteSerializer(serializers.ModelSerializer):
    """Сериалайзер ограничений по видам деятельности."""

    restrictions = BaseRestrictionSerializer(many=True)
    infrastructures = BaseInfrastructureSerializer(many=True)
    privileges = BasePrivilegeSerializer(many=True)

    class Meta:
        model = SpecializedSite
        fields = (
            'id',
            'investment_object',
            'external_id',
            'sez',
            'tad',
            'region',
            'nearest_cities',
            'number_residents',
            'document_url',
            'year_formation',
            'validity',
            'restrictions',
            'infrastructures',
            'additional_services',
            'object_administrator_name',
            'address',
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
        )
