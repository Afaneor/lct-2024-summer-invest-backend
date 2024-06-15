from server.apps.investment_object.models import ReadyBusiness
from server.apps.services.serializers import ModelSerializerWithPermission


class ReadyBusinessSerializer(ModelSerializerWithPermission):
    """Сериалайзер готового бизнеса."""

    class Meta:
        model = ReadyBusiness
        fields = (
            'id',
            'investment_object',
            'external_id',
            'description',
            'extra_data',
            'permission_rules',
            'created_at',
            'updated_at',
        )
