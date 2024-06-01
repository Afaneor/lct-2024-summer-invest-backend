from taggit.serializers import TagListSerializerField

from server.apps.hincal.models import Equipment
from server.apps.services.serializers import ModelSerializerWithPermission


class EquipmentSerializer(ModelSerializerWithPermission):
    """Сериалайзер оборудования."""

    tags = TagListSerializerField()

    class Meta(object):
        model = Equipment
        fields = (
            'id',
            'name',
            'cost',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )
