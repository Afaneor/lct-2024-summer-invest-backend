from rest_framework import serializers

from server.apps.personal_cabinet.models.message import Message
from server.apps.services.serializers import ModelSerializerWithPermission


class MessageSerializer(ModelSerializerWithPermission):
    """
    Сериалайзер сообщения.
    """

    class Meta:
        model = Message
        fields = (
            'id',
            'owner_type',
            'selection_request',
            'text',
            'parent',
            'permission_rules',
            'created_at',
            'updated_at',
        )


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
            'parent',
        )
