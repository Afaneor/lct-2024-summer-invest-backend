import django_filters

from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet
from server.apps.support.api.serializers import ProblemCategorySerializer
from server.apps.support.models import ProblemCategory


class ProblemCategoryFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инфраструктуры."""

    class Meta:
        model = ProblemCategory
        fields = (
            'id',
            'name',
        )


class ProblemCategoryViewSet(BaseReadOnlyViewSet):
    """Инфраструктура."""

    serializer_class = ProblemCategorySerializer
    queryset = ProblemCategory.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ProblemCategoryFilter
