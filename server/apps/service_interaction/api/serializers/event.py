from server.apps.service_interaction.models import Event
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


class ListEventSerializer(ModelSerializerWithPermission):
    """Сериалайзер событий."""

    user = BaseUserSerializer()

    class Meta:
        model = Event
        fields = (
            'id',
            'user',
            'text',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class DetailEventSerializer(ModelSerializerWithPermission):
    """Сериалайзер события."""

    user = BaseUserSerializer()

    class Meta:
        model = Event
        fields = (
            'id',
            'user',
            'text',
            'content_type_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )
