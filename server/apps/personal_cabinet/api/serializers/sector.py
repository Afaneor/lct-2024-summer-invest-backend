from taggit.serializers import TagListSerializerField

from server.apps.personal_cabinet.models import Sector
from server.apps.services.serializers import ModelSerializerWithPermission


class SectorSerializer(ModelSerializerWithPermission):
    """Сериалайзер оборудования."""

    tags = TagListSerializerField()

    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
            'slug',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class BaseSectorSerializer(ModelSerializerWithPermission):
    """Сериалайзер оборудования."""

    tags = TagListSerializerField()

    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
            'slug',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )
