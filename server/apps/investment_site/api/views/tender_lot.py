import django_filters

from server.apps.investment_site.api.serializers import TenderLotSerializer
from server.apps.investment_site.models import TenderLot
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class TenderLotFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр лотов тендеров."""

    class Meta(object):
        model = TenderLot
        fields = (
            'id',
            'tender_lot_id',
            'name',
            'detail_url',
        )


class TenderLotViewSet(BaseReadOnlyViewSet):
    """Лот тендера."""

    serializer_class = TenderLotSerializer
    queryset = TenderLot.objects.all()
    search_fields = (
        'tender__tender_id',
        'tender_lot_id',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = TenderLotFilter

