import django_filters

from server.apps.investment_object.api.serializers import (
    EconomicActivitySerializer,
)
from server.apps.investment_object.models import EconomicActivity
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class EconomicActivityFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр экономической деятельности."""

    class Meta:
        model = EconomicActivity
        fields = (
            'id',
            'code',
            'name',
        )


class EconomicActivityViewSet(RetrieveListViewSet):
    """Экономическая деятельность."""

    serializer_class = EconomicActivitySerializer
    queryset = EconomicActivity.objects.all()
    search_fields = (
        'code',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = EconomicActivityFilter
