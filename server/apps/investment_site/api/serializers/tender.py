from server.apps.investment_site.models import Tender
from server.apps.services.serializers import ModelSerializerWithPermission


class TenderSerializer(ModelSerializerWithPermission):
    """Сериалайзер тендеров."""

    class Meta(object):
        model = Tender
        fields = (
            'id',
            'tender_id',
            'bidding_type',
            'extra_data',
            'detail_url',
            'created_at',
            'updated-at',
        )
