import django_filters

from server.apps.investment_object.api.serializers import (
    ReadyBusinessSerializer,
)
from server.apps.investment_object.models import ReadyBusiness
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class ReadyBusinessFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр готового бизнеса."""

    class Meta:
        model = ReadyBusiness
        fields = (
            'id',
            'external_id',
            'name',
        )


class ReadyBusinessViewSet(BaseReadOnlyViewSet):
    """Готовый бизнес."""

    serializer_class = ReadyBusinessSerializer
    queryset = ReadyBusiness.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ReadyBusinessFilter
