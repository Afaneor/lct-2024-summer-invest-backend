import django_filters

from server.apps.investment_object.api.serializers import (
    InfrastructureSerializer,
)
from server.apps.investment_object.models import Infrastructure
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class InfrastructureFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инфраструктуры."""

    class Meta:
        model = Infrastructure
        fields = (
            'id',
            'name',
        )


class InfrastructureViewSet(BaseReadOnlyViewSet):
    """Инфраструктура."""

    serializer_class = InfrastructureSerializer
    queryset = Infrastructure.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InfrastructureFilter
