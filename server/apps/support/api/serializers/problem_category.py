from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.api.serializers import BaseProblemSubcategorySerializer
from server.apps.support.models import ProblemCategory


class ProblemCategorySerializer(ModelSerializerWithPermission):
    """Сериалайзер категорий проблем."""

    problem_subcategories = BaseProblemSubcategorySerializer(many=True)

    class Meta:
        model = ProblemCategory
        fields = (
            'id',
            'name',
            'problem_subcategories',
            'permission_rules',
            'created_at',
            'updated_at',
        )
