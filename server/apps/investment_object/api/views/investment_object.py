import django_filters

from server.apps.investment_object.api.serializers import (
    InvestmentObjectSerializer,
)
from server.apps.investment_object.models import InvestmentObject
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class InvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'object_type',
            'url',
        )


class InvestmentObjectViewSet(BaseReadOnlyViewSet):
    """Инвестиционные площадки."""

    serializer_class = InvestmentObjectSerializer
    queryset = InvestmentObject.objects.all()
    search_fields = (
        'investment_site_id',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InvestmentObjectFilter

