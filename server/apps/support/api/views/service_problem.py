import django_filters

from server.apps.support.api.serializers import (
    ServiceProblemSerializer,
)
from server.apps.support.models import ServiceProblem
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class ServiceProblemFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инфраструктуры."""

    class Meta:
        model = ServiceProblem
        fields = (
            'id',
            'name',
        )


class ServiceProblemViewSet(BaseReadOnlyViewSet):
    """Инфраструктура."""

    serializer_class = ServiceProblemSerializer
    queryset = ServiceProblem.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ServiceProblemFilter
