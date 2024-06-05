import django_filters

from server.apps.investment_object.api.serializers import TenderSerializer
from server.apps.investment_object.models import Tender
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class TenderFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр тендеров."""

    class Meta:
        model = Tender
        fields = (
            'id',
            'tender_id',
            'bidding_type',
            'detail_url',
        )


class TenderViewSet(BaseReadOnlyViewSet):
    """Тендер."""

    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
    search_fields = (
        'tender_id',
        'bidding_type',
    )
    ordering_fields = '__all__'
    filterset_class = TenderFilter

