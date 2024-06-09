from rest_framework import serializers

from server.apps.service_interaction.models import Feedback
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.user.api.serializers import BaseUserSerializer


class FeedbackSerializer(ModelSerializerWithPermission):
    """Сериалайзер отзывов."""

    user = BaseUserSerializer()

    class Meta:
        model = Feedback
        fields = (
            'id',
            'user',
            'text',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class CreateFeedbackSerializer(serializers.ModelSerializer):
    """Сериалайзер создания отзывов."""

    class Meta:
        model = Feedback
        fields = (
            'id',
            'text',
            'content_type',
            'object_id',
        )
