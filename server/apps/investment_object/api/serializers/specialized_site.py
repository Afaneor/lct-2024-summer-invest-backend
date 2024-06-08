from server.apps.investment_object.api.serializers import (
    BaseEconomicActivitySerializer,
    BaseInfrastructureSerializer,
    BasePrivilegeSerializer,
    BaseRestrictionSerializer,
)
from server.apps.investment_object.models import SpecializedSite
from server.apps.services.serializers import ModelSerializerWithPermission


class SpecializedSiteSerializer(ModelSerializerWithPermission):
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
            'permission_rules',
            'created_at',
            'updated_at',
        )
