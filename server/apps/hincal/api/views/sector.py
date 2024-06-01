import django_filters

from server.apps.hincal.api.serializers import SectorSerializer
from server.apps.hincal.models import Sector
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet


class SectorFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр отраслей."""

    name = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Sector
        fields = (
            'id',
            'name',
            'slug',
        )


class SectorViewSet(BaseReadOnlyViewSet):
    """Отрасль. Просмотр."""

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
    search_fields = (
        'name',
        'slug',
    )
    ordering_fields = '__all__'
    filterset_class = SectorFilter

    def get_queryset(self):
        """Выдача отраслей.

        Все видят все оборудование.
        """
        return super().get_queryset()
