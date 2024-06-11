from rest_framework import serializers

from server.apps.personal_cabinet.api.serializers import BaseMessageSerializer
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


class SelectionRequestSerializer(ModelSerializerWithPermission):
    """
    Сериалайзер запросов на подбор площадок.
    """

    user = BaseUserSerializer()
    bot_filter = serializers.SerializerMethodField()

    class Meta:
        model = SelectionRequest
        fields = (
            'id',
            'user',
            'anonymous_user_id',
            'bot_filter',
            'is_actual',
            'is_bot_response_waiting',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_bot_filter(self, selection_request: SelectionRequest):
        """Фильтры для объектов инвестирования, мер поддержки, проблем."""
        message = selection_request.messages.filter(
            bot_filter__isnull=False,
        ).order_by('created_at').first()
        return message.bot_filter if message else None


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
