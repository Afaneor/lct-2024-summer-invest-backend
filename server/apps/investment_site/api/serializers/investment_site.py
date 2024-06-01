from server.apps.investment_site.models import InvestmentSite
from server.apps.services.serializers import ModelSerializerWithPermission


class InvestmentSiteSerializer(ModelSerializerWithPermission):
    """Сериалайзер инвестиционных площадок."""

    class Meta(object):
        model = InvestmentSite
        fields = (
            'id',
            'investment_site_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'investment_object_type',
            'detail_url',
            'extra_data',
            'coordinates',
            'created_at',
            'updated-at',
        )
