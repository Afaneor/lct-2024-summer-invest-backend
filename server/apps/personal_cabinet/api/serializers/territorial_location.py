from taggit.serializers import TagListSerializerField

from server.apps.personal_cabinet.models import TerritorialLocation
from server.apps.services.serializers import ModelSerializerWithPermission


class TerritorialLocationSerializer(ModelSerializerWithPermission):
    """Сериалайзер территориального расположения."""

    tags = TagListSerializerField()

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'shot_name',
            'full_name',
            'slug',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class BaseTerritorialLocationSerializer(ModelSerializerWithPermission):
    """Сериалайзер территориального расположения для других сериализаторов."""

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'shot_name',
            'full_name',
            'permission_rules',
            'created_at',
            'updated_at',
        )
