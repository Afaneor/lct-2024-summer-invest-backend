from rest_framework import serializers

from server.apps.investment_object.models import InvestmentObject
from server.apps.services.serializers import ModelSerializerWithPermission


class BaseInvestmentObjectSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер инвестиционных площадок."""

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'external_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'object_type',
            'detail_url',
            'extra_data',
            'longitude',
            'latitude',
        )


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
            'detail_url',
            'extra_data',
            'longitude',
            'latitude',
            'created_at',
            'updated_at',
        )
