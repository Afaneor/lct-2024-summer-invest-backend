from rest_framework import serializers

from server.apps.service_interaction.models import Comment
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


class CommentSerializer(ModelSerializerWithPermission):
    """Сериалайзер отзывов."""

    user = BaseUserSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
            'content_type',
            'object_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class CreateCommentSerializer(serializers.ModelSerializer):
    """Сериалайзер создания отзывов."""

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'content_type',
            'object_id',
        )
