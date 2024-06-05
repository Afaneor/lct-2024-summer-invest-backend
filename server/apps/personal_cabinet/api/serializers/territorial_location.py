from taggit.serializers import TagListSerializerField

from server.apps.personal_cabinet.models import TerritorialLocation
from server.apps.services.serializers import ModelSerializerWithPermission


class TerritorialLocationSerializer(ModelSerializerWithPermission):
    """Сериалайзер территориального расположения."""

    tags = TagListSerializerField()

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'shot_name',
            'full_name',
            'slug',
            'avg_land_cadastral_value',
            'avg_land_lease_costs',
            'avg_land_purchase_costs',
            'avg_property_cadastral_value',
            'avg_property_lease_costs',
            'avg_property_purchase_costs',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )



class BaseTerritorialLocationSerializer(ModelSerializerWithPermission):
    """Сериалайзер территориального расположения для других сериализаторов."""

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'shot_name',
            'full_name',
            'permission_rules',
            'created_at',
            'updated_at',
        )
