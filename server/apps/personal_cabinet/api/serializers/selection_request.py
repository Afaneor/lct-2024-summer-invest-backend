from rest_framework import serializers

from server.apps.personal_cabinet.api.serializers import BaseMessageSerializer
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


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

    user = BaseUserSerializer()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = SelectionRequest
        fields = (
            'id',
            'user',
            'anonymous_user_id',
            'messages',
            'is_actual',
            'is_bot_response_waiting',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_messages(self, selection_request: SelectionRequest):
        """Сообщения для запроса."""
        return BaseMessageSerializer(
            selection_request.messages.all().order_by('id'),
            many=True,
            context=self.context,
        ).data
