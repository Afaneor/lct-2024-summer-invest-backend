from server.apps.investment_object.models import Restriction
from server.apps.services.serializers import ModelSerializerWithPermission


class RestrictionSerializer(ModelSerializerWithPermission):
    """Сериалайзер ограничений по видам деятельности."""

    class Meta:
        model = Restriction
        fields = (
            'id',
            'name',
            'permission_rules',
            'created_at',
            'updated_at',
        )
