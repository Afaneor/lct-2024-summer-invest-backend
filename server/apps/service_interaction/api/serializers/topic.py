from typing import Optional

from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from server.apps.service_interaction.api.serializers.base_data import (
    BasePostSerializer,
)
from server.apps.service_interaction.models import Topic
from server.apps.services.serializers import ModelSerializerWithPermission


class ListTopicSerializer(ModelSerializerWithPermission):
    """Сериалайзер темы."""

    post_count = serializers.SerializerMethodField()
    last_post = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
            'description',
            'permission_rules',
            'post_count',
            'last_post',
            'created_at',
            'updated_at',
        )

    def get_post_count(self, topic: Topic) -> int:
        """Количество постов в теме."""
        return topic.posts.count()

    def get_last_post(self, topic: Topic) -> Optional[ReturnDict]:
        """Информация о последнем сообщении."""
        post = topic.posts.first()
        if post:
            return BasePostSerializer(
                instance=topic.posts.first(),
                context=self.context,
            ).data
        return None

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
