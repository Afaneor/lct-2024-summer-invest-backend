import django_filters

from server.apps.personal_cabinet.api.serializers import (
    TerritorialLocationSerializer,
)
from server.apps.personal_cabinet.models import TerritorialLocation
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet


class TerritorialLocationFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр территориального расположения."""

    shot_name = django_filters.CharFilter(lookup_expr='icontains')
    full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'shot_name',
            'full_name',
        )


class TerritorialLocationViewSet(BaseReadOnlyViewSet):
    """Территориальное расположение. Просмотр."""

    serializer_class = TerritorialLocationSerializer
    queryset = TerritorialLocation.objects.prefetch_related('tags')
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = TerritorialLocationFilter

    def get_queryset(self):
        """Выдача территориального расположения.

        Все видят все территориальные расположения.
        """
        return super().get_queryset()
