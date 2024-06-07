from server.apps.investment_object.models import Privilege
from server.apps.services.serializers import ModelSerializerWithPermission


class PrivilegeSerializer(ModelSerializerWithPermission):
    """Сериалайзер льгот."""

    class Meta:
        model = Privilege
        fields = (
            'id',
            'name',
            'permission_rules',
            'created_at',
            'updated_at',
        )
