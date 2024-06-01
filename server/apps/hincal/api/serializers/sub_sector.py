from server.apps.hincal.models import SubSector
from server.apps.services.serializers import ModelSerializerWithPermission


class SubSectorSerializer(ModelSerializerWithPermission):
    """Сериалайзер подотрасли."""

    class Meta(object):
        model = SubSector
        fields = (
            'id',
            'name',
            'slug',
            'permission_rules',
            'created_at',
            'updated_at',
        )
