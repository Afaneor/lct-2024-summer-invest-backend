from rest_framework import serializers

from server.apps.investment_object.api.serializers import (
    BaseInvestmentObjectSerializer,
)
from server.apps.personal_cabinet.models import SelectedEntity
from server.apps.services.serializers import ModelSerializerWithPermission


class SelectedEntitySerializer(ModelSerializerWithPermission):
    """
    Сериалайзер подобранного инвестиционного объекта.
    """

    investment_object = BaseInvestmentObjectSerializer()

    class Meta:
        model = SelectedEntity
        fields = (
            'id',
            'investment_object',
            'selection_request',
            'message',
            'is_relevant',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class UpdateSelectedEntitySerializer(serializers.ModelSerializer):
    """
    Сериалайзер изменения подобранного инвестиционного объекта.
    """

    class Meta:
        model = SelectedEntity
        fields = (
            'id',
            'is_relevant',
        )
