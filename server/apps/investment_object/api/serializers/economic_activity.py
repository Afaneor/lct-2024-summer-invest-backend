from rest_framework import serializers

from server.apps.investment_object.models import EconomicActivity
from server.apps.services.serializers import ModelSerializerWithPermission


class EconomicActivitySerializer(ModelSerializerWithPermission):
    """Сериалайзер экономической деятельности."""

    class Meta:
        model = EconomicActivity
        fields = (
            'id',
            'code',
            'parent_code',
            'section',
            'name',
            'comment',
            'permission_rules',
            'created_at',
            'updated_at',
        )
