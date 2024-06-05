from rest_framework import serializers

from server.apps.investment_object.api.serializers import (
    BaseInvestmentObjectSerializer,
)
from server.apps.personal_cabinet.models import SelectedInvestmentObject
from server.apps.services.serializers import ModelSerializerWithPermission


class SelectedInvestmentObjectSerializer(ModelSerializerWithPermission):
    """
    Сериалайзер подобранного инвестиционного объекта.
    """

    investment_object = BaseInvestmentObjectSerializer()

    class Meta:
        model = SelectedInvestmentObject
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


class UpdateSelectedInvestmentObjectSerializer(serializers.ModelSerializer):
    """
    Сериалайзер изменения подобранного инвестиционного объекта.
    """

    class Meta:
        model = SelectedInvestmentObject
        fields = (
            'id',
            'is_relevant',
        )
