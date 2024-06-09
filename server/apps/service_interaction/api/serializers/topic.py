from server.apps.service_interaction.models import Topic
from server.apps.services.serializers import ModelSerializerWithPermission


class TopicSerializer(ModelSerializerWithPermission):
    """Сериалайзер темы."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'description',
            'permission_rules',
            'created_at',
            'updated_at',
        )
