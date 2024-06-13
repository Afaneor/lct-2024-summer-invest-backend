from rest_framework import serializers

from server.apps.service_interaction.models import Comment, Post, Topic
from server.apps.user.api.serializers import BaseUserSerializer


class BasePostSerializer(serializers.ModelSerializer):
    """Сериалайзер поста к теме."""

    user = BaseUserSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'parent',
            'text',
            'created_at',
        )


class BaseTopicSerializer(serializers.ModelSerializer):
    """Сериалайзер темы."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'shot_description',
            'description',
        )


class BaseCommentSerializer(serializers.ModelSerializer):
    """Сериалайзер отзывов."""

    user = BaseUserSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
        )
