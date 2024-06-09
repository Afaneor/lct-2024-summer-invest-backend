from rest_framework import serializers

from server.apps.service_interaction.models import Comment, Post, Topic
from server.apps.user.api.serializers import BaseUserSerializer


class BasePostSerializer(serializers.Serializer):
    """Сериалайзер поста к теме."""

    user = BaseUserSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'parent',
            'text',
        )


class BaseTopicSerializer(serializers.Serializer):
    """Сериалайзер темы."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'description',
        )


class BaseCommentSerializer(serializers.Serializer):
    """Сериалайзер отзывов."""

    user = BaseUserSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
        )
