from rest_framework import serializers

from server.apps.service_interaction.api.serializers.base_data import (
    BaseCommentSerializer,
    BasePostSerializer,
)
from server.apps.service_interaction.models import Comment, Topic
from server.apps.services.serializers import ModelSerializerWithPermission


class ListTopicSerializer(ModelSerializerWithPermission):
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


class DetailTopicSerializer(ModelSerializerWithPermission):
    """Сериалайзер темы."""

    posts = BasePostSerializer(many=True)

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'description',
            'posts',
            'content_type_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )
