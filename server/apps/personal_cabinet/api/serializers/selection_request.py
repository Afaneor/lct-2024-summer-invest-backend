from rest_framework import serializers

from server.apps.investment_object.api.serializers import (
    BaseInvestmentObjectSerializer,
)
from server.apps.personal_cabinet.api.serializers import BaseMessageSerializer
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseInfoUserSerializer


class CreateSelectionRequestSerializer(serializers.ModelSerializer):
    """
    Сериалайзер создания запросов на подбор площадок.
    """

    class Meta:
        model = SelectionRequest
        fields = (
            'id',
            'anonymous_user_id',
        )


class SelectionRequestSerializer(ModelSerializerWithPermission):
    """
    Сериалайзер запросов на подбор площадок.
    """

    user = BaseInfoUserSerializer()
    investment_objects = BaseInvestmentObjectSerializer(many=True)
    messages = BaseMessageSerializer(many=True)

    class Meta:
        model = SelectionRequest
        fields = (
            'id',
            'user',
            'anonymous_user_id',
            'investment_objects',
            'is_actual',
            'permission_rules',
            'created_at',
            'updated_at',
        )
