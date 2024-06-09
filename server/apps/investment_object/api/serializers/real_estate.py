from server.apps.investment_object.api.serializers import (
    BaseInfrastructureSerializer,
)
from server.apps.investment_object.models import RealEstate
from server.apps.services.serializers import ModelSerializerWithPermission


class RealEstateSerializer(ModelSerializerWithPermission):
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
            'permission_rules',
            'created_at',
            'updated_at',
        )
