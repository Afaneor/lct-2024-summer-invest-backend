from server.apps.investment_object.models import TenderLot
from server.apps.services.serializers import ModelSerializerWithPermission


class TenderLotSerializer(ModelSerializerWithPermission):
    """Сериалайзер лот тендера."""

    class Meta:
        model = TenderLot
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
