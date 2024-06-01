import django_filters

from server.apps.hincal.api.serializers import EquipmentSerializer
from server.apps.hincal.models import Equipment
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet


class EquipmentFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр отчетов."""

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Equipment
        fields = (
            'id',
            'name',
            'cost',
        )


class EquipmentViewSet(BaseReadOnlyViewSet):
    """Оборудование. Просмотр."""

    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = EquipmentFilter

    def get_queryset(self):
        """Выдача оборудования.

        Все видят все оборудование.
        """
        return super().get_queryset()
