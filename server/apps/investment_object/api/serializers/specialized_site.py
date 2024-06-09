from server.apps.investment_object.api.serializers import (
    BaseInfrastructureSerializer,
    BasePrivilegeSerializer,
    BaseRestrictionSerializer,
)
from server.apps.investment_object.models import SpecializedSite
from server.apps.services.serializers import ModelSerializerWithPermission


class SpecializedSiteSerializer(ModelSerializerWithPermission):
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
            'permission_rules',
            'created_at',
            'updated_at',
        )
