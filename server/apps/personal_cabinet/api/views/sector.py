import django_filters

from server.apps.personal_cabinet.api.serializers import SectorSerializer
from server.apps.personal_cabinet.models import Sector
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class SectorFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр отраслей."""

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
        )


class SectorViewSet(RetrieveListViewSet):
    """Отрасль. Просмотр."""

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = SectorFilter

    def get_queryset(self):
        """Выдача отраслей.

        Все видят все оборудование.
        """
        return super().get_queryset()
