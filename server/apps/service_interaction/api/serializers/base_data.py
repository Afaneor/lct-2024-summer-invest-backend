from rest_framework import serializers

from server.apps.service_interaction.models import Topic


class BaseTopicSerializer(serializers.Serializer):
    """Сериалайзер темы."""

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'description',
        )
