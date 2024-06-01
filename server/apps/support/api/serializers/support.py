from taggit.serializers import TagListSerializerField

from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.models import Support


class SupportSerializer(ModelSerializerWithPermission):
    """Сериалайзер мер поддержки."""

    tags = TagListSerializerField()

    class Meta(object):
        model = Support
        fields = (
            'id',
            'preview_image',
            'title',
            'text',
            'amount',
            'site',
            'extra_data',
            'is_actual',
            'tags',
            'created_at',
            'updated_at',
            'permission_rules',
        )


class BaseSupportSerializer(ModelSerializerWithPermission):
    """Сериалайзер мер поддержки для других сериалайзеров."""

    class Meta(object):
        model = Support
        fields = (
            'id',
            'preview_image',
            'title',
            'text',
            'amount',
            'site',
            'extra_data',
            'is_actual',
        )
