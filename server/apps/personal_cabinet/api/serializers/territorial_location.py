from server.apps.personal_cabinet.models import TerritorialLocation
from server.apps.services.serializers import ModelSerializerWithPermission


class TerritorialLocationSerializer(ModelSerializerWithPermission):
    """Сериалайзер территориального расположения."""

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'short_name',
            'full_name',
            'permission_rules',
            'created_at',
            'updated_at',
        )

