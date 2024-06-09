from rest_framework import serializers

from server.apps.service_interaction.api.serializers import BaseTopicSerializer
from server.apps.service_interaction.models import Post
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


class PostSerializer(ModelSerializerWithPermission):
    """Сериалайзер отзывов."""

    user = BaseUserSerializer()
    topic = BaseTopicSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'topic',
            'parent',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class CreatePostSerializer(ModelSerializerWithPermission):
    """Сериалайзер создания отзывов."""

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'topic',
            'parent',
        )
