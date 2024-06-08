from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.models import ServiceProblem


class ServiceProblemSerializer(ModelSerializerWithPermission):
    """Сериалайзер возможных проблем."""

    class Meta:
        model = ServiceProblem
        fields = (
            'id',
            'external_category_id',
            'external_subcategory_id',
            'external_theme_id',
            'name',
            'category_name',
            'subcategory_name',
            'theme_name',
            'additional_info',
            'url',
            'permission_rules',
            'created_at',
            'updated_at',
        )
