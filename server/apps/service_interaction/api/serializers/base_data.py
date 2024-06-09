from rest_framework import serializers

from server.apps.service_interaction.models import Feedback, Topic
from server.apps.user.api.serializers import BaseUserSerializer


class BaseTopicSerializer(serializers.Serializer):
    """Сериалайзер темы."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'description',
        )


class BaseUserSerialzier:
    pass


class BaseFeedbackSerializer(serializers.Serializer):
    """Сериалайзер отзывов."""

    user = BaseUserSerializer()

    class Meta:
        model = Feedback
        fields = (
            'id',
            'user',
            'text',
        )
