from server.apps.service_interaction.models import Event
from server.apps.services.serializers import ModelSerializerWithPermission


class ListEventSerializer(ModelSerializerWithPermission):
    """Сериалайзер событий."""

    class Meta:
        model = Event
        fields = (
            'id',
            'photo',
            'name',
            'event_datetime',
            'description',
            'event_type',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class DetailEventSerializer(ModelSerializerWithPermission):
    """Сериалайзер события."""

    class Meta:
        model = Event
        fields = (
            'id',
            'photo',
            'name',
            'event_datetime',
            'description',
            'event_type',
            'content_type_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )
