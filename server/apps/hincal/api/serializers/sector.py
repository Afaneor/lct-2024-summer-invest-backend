from taggit.serializers import TagListSerializerField

from server.apps.hincal.models import Sector
from server.apps.services.serializers import ModelSerializerWithPermission


class SectorSerializer(ModelSerializerWithPermission):
    """Сериалайзер оборудования."""

    tags = TagListSerializerField()

    class Meta(object):
        model = Sector
        fields = (
            'id',
            'name',
            'slug',
            'possible_income_on_market',
            'possible_income_from_patent',
            'average_salary_of_staff',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class BaseSectorSerializer(ModelSerializerWithPermission):
    """Сериалайзер оборудования."""

    tags = TagListSerializerField()

    class Meta(object):
        model = Sector
        fields = (
            'id',
            'name',
            'slug',
            'possible_income_from_patent',
            'possible_income_on_market',
            'average_salary_of_staff',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )