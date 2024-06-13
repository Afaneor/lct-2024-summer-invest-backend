from rest_framework import serializers

from server.apps.service_interaction.models import Event
from server.apps.services.serializers import ModelSerializerWithPermission


class ListEventSerializer(ModelSerializerWithPermission):
    """Сериалайзер событий."""

    event_type_label = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'photo',
            'name',
            'event_datetime',
            'description',
            'event_type',
            'event_type_label',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_availability_label(
        self,
        event: Event,
    ):
        """Подпись к event_type."""
        return event.get_event_type_display()


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
