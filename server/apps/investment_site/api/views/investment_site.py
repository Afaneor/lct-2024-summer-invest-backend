import django_filters

from server.apps.investment_site.api.serializers import (
    InvestmentSiteSerializer,
)
from server.apps.investment_site.models import InvestmentSite
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class InvestmentSiteFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    class Meta(object):
        model = InvestmentSite
        fields = (
            'id',
            'name',
            'investment_object_type',
            'detail_url',
        )


class InvestmentSiteViewSet(BaseReadOnlyViewSet):
    """Инвестиционные площадки."""

    serializer_class = InvestmentSiteSerializer
    queryset = InvestmentSite.objects.all()
    search_fields = (
        'investment_site_id',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InvestmentSiteFilter

