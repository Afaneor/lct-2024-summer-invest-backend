import django_filters

from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet
from server.apps.support.api.serializers import (
    DetailServiceSupportSerializer,
    ListServiceSupportSerializer,
)
from server.apps.support.models import ServiceSupport


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

    serializer_class = DetailServiceSupportSerializer
    list_serializer_class = ListServiceSupportSerializer
    queryset = ServiceSupport.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ServiceSupportFilter
