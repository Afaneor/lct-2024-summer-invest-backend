from server.apps.investment_object.models import TenderLot
from server.apps.services.serializers import ModelSerializerWithPermission


class TenderLotSerializer(ModelSerializerWithPermission):
    """Сериалайзер лот тендера."""

    class Meta:
        model = TenderLot
        fields = (
            'id',
            'investment_object',
            'bidding_type',
            'description',
            'extra_data',
            'url',
            'permission_rules',
            'created_at',
            'updated_at',
        )
