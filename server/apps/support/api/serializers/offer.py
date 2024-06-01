from taggit.serializers import TagListSerializerField

from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.models import Offer


class OfferSerializer(ModelSerializerWithPermission):
    """Сериалайзер партнерских предложений."""

    tags = TagListSerializerField()

    class Meta(object):
        model = Offer
        fields = (
            'id',
            'title',
            'text',
            'site',
            'interest_rate',
            'loan_term',
            'amount',
            'extra_data',
            'tags',
            'created_at',
            'updated_at',
            'permission_rules',
        )


class BaseOfferSerializer(ModelSerializerWithPermission):
    """Сериалайзер партнерских предложений для других сериалайзеров."""

    class Meta(object):
        model = Offer
        fields = (
            'id',
            'title',
            'text',
            'site',
            'interest_rate',
            'loan_term',
            'amount',
            'extra_data',
        )
