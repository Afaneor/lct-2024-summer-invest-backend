from server.apps.investment_object.models import TenderLot
from server.apps.services.serializers import ModelSerializerWithPermission


class TenderLotSerializer(ModelSerializerWithPermission):
    """Сериалайзер лот тендера."""

    class Meta:
        model = TenderLot
        fields = (
            'id',
            'tender',
            'tender_lot_id',
            'name',
            'description',
            'extra_data',
            'url',
            'created_at',
            'updated_at',
        )
