from taggit.serializers import TagListSerializerField

from server.apps.blog.models import Post
from server.apps.services.serializers import ModelSerializerWithPermission


class PostSerializer(ModelSerializerWithPermission):
    """Сериалайзер постов."""

    tags = TagListSerializerField()

    class Meta(object):
        model = Post
        fields = (
            'id',
            'preview_image',
            'title',
            'text',
            'tags',
            'is_published',
            'created_at',
            'updated_at',
            'permission_rules',
        )
