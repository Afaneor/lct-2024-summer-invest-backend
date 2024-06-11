import django_filters

from server.apps.personal_cabinet.api.serializers import (
    TerritorialLocationSerializer,
)
from server.apps.personal_cabinet.models import TerritorialLocation
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class TerritorialLocationFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр территориального расположения."""

    short_name = django_filters.CharFilter(lookup_expr='icontains')
    full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'short_name',
            'full_name',
        )


class TerritorialLocationViewSet(RetrieveListViewSet):
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
