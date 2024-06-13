from rest_framework import serializers

from server.apps.personal_cabinet.models.message import Message
from server.apps.services.serializers import ModelSerializerWithPermission


class MessageSerializer(ModelSerializerWithPermission):
    """
    Сериалайзер сообщения.
    """

    owner_type_label = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = (
            'id',
            'owner_type',
            'selection_request',
            'text',
            'user_filter',
            'bot_filter',
            'parent',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_owner_type_label(
        self,
        message: Message,
    ):
        """Подпись к owner_type."""
        return message.get_owner_type_display()


class CreateMessageSerializer(ModelSerializerWithPermission):
    """
    Сериалайзер создания сообщения.
    """

    class Meta:
        model = Message
        fields = (
            'id',
            'owner_type',
            'selection_request',
            'text',
            'user_filter',
            'bot_filter',
            'parent',
        )
