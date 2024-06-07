from server.apps.investment_object.models import InvestmentObject
from server.apps.services.serializers import ModelSerializerWithPermission


class InvestmentObjectSerializer(ModelSerializerWithPermission):
    """Сериалайзер инвестиционных площадок."""

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'external_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'object_type',
            'url',
            'extra_data',
            'longitude',
            'latitude',
            'permission_rules',
            'created_at',
            'updated_at',
        )
