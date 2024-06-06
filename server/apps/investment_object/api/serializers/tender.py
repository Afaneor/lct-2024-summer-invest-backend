from server.apps.investment_object.models import Tender
from server.apps.services.serializers import ModelSerializerWithPermission


class TenderSerializer(ModelSerializerWithPermission):
    """Сериалайзер тендеров."""

    class Meta:
        model = Tender
        fields = (
            'id',
            'tender_id',
            'bidding_type',
            'extra_data',
            'url',
            'created_at',
            'updated_at',
        )
