import django_filters

from server.apps.hincal.api.serializers import SubSectorSerializer
from server.apps.hincal.models import SubSector
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet


class SubSectorFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр подотрасли."""

    name = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = SubSector
        fields = (
            'id',
            'name',
            'slug',
        )


class SubSectorViewSet(BaseReadOnlyViewSet):
    """Подотрасль. Просмотр."""

    serializer_class = SubSectorSerializer
    queryset = SubSector.objects.all()
    search_fields = (
        'name',
        'slug',
    )
    ordering_fields = '__all__'
    filterset_class = SubSectorFilter

    def get_queryset(self):
        """Выдача подотраслей.

        Все видят все подотрасли.
        """
        return super().get_queryset()
