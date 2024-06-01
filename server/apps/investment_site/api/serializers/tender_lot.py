from server.apps.investment_site.models import TenderLot
from server.apps.services.serializers import ModelSerializerWithPermission


class TenderLotSerializer(ModelSerializerWithPermission):
    """Сериалайзер лот тендера."""

    class Meta(object):
        model = TenderLot
        fields = (
            'id',
            'tender',
            'tender_lot_id',
            'name',
            'description',
            'extra_data',
            'detail_url',
            'created_at',
            'updated-at',
        )
