from server.apps.investment_object.models import EconomicActivity
from server.apps.services.serializers import ModelSerializerWithPermission


class EconomicActivitySerializer(ModelSerializerWithPermission):
    """Сериалайзер экономической деятельности."""

    class Meta:
        model = EconomicActivity
        fields = (
            'id',
            'code',
            'name',
            'permission_rules',
            'created_at',
            'updated_at',
        )
