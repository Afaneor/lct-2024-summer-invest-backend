from server.apps.hincal.api.serializers.territorial_location import (
    BaseTerritorialLocationSerializer,
)
from server.apps.hincal.models import Business
from server.apps.services.serializers import ModelSerializerWithPermission


class BusinessSerializer(ModelSerializerWithPermission):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    territorial_location = BaseTerritorialLocationSerializer()

    class Meta(object):
        model = Business
        fields = (
            'id',
            'user',
            'position',
            'type',
            'inn',
            'sector',
            'sub_sector',
            'territorial_location',
            'hid',
            'short_business_name',
            'full_business_name',
            'management_name',
            'management_position',
            'full_opf',
            'short_opf',
            'okved',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'country',
            'region',
            'city_area',
            'city_district',
            'phone',
            'email',
            'site',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class BaseBusinessSerializer(ModelSerializerWithPermission):
    """Информация о бизнесе для отчета."""

    territorial_location = BaseTerritorialLocationSerializer()

    class Meta(object):
        model = Business
        fields = (
            'type',
            'inn',
            'sector',
            'sub_sector',
            'territorial_location',
            'short_business_name',
            'full_business_name',
            'management_name',
            'management_position',
            'full_opf',
            'short_opf',
            'okved',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'country',
            'region',
            'city_area',
            'city_district',
            'phone',
            'email',
            'site',
        )
