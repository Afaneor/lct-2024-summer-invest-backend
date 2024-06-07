from server.apps.investment_object.api.serializers import (
    BaseEconomicActivitySerializer,
    BaseInfrastructureSerializer,
)
from server.apps.investment_object.models import RealEstate
from server.apps.services.serializers import ModelSerializerWithPermission


class RealEstateSerializer(ModelSerializerWithPermission):
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
            'permission_rules',
            'created_at',
            'updated_at',
        )
