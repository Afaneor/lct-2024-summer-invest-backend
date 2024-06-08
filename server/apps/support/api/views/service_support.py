import django_filters

from server.apps.support.api.serializers import (
    ServiceSupportSerializer,
)
from server.apps.support.models import ServiceSupport
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class ServiceSupportFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инфраструктуры."""

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
            'name',
        )


class ServiceSupportViewSet(BaseReadOnlyViewSet):
    """Инфраструктура."""

    serializer_class = ServiceSupportSerializer
    queryset = ServiceSupport.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ServiceSupportFilter
