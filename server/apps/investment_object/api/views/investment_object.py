import django_filters
from django.db import models

from server.apps.investment_object.api.serializers import (
    InvestmentObjectSerializer,
)
from server.apps.investment_object.models import InvestmentObject
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListCreateViewSet


class InvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    economic_activity = django_filters.CharFilter(
        method='filter_economic_activity',
        label='Фильтрация по экономической деятельности',
    )

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'object_type',
            'economic_activity',
        )

    def filter_economic_activity(self, queryset, name, value):
        """Фильтрация по экономической деятельности."""
        return queryset.filter(
            models.Q(specialized_site__economic_activities__name__icontains=value) |
            models.Q(real_estate__economic_activities__name__icontains=value)
        )


class InvestmentObjectViewSet(RetrieveListCreateViewSet):
    """Инвестиционные площадки."""

    serializer_class = InvestmentObjectSerializer
    queryset = InvestmentObject.objects.all()
    search_fields = (
        'external_id',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InvestmentObjectFilter

