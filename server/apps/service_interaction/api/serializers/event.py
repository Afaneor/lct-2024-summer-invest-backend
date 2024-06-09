from rest_framework import serializers

from server.apps.service_interaction.api.serializers.base_data import (
    BaseCommentSerializer,
)
from server.apps.service_interaction.models import Comment, Event
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

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'photo',
            'name',
            'event_datetime',
            'description',
            'event_type',
            'comments',
            'content_type_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_comments(self, event: Event):
        """Комментарии к объекту."""
        return BaseCommentSerializer(
            Comment.objects.filter(
                object_id=event.id,
                content_type_id=event.content_type_id,
            ),
            many=True,
        ).data
