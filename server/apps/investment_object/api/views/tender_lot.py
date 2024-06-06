import django_filters

from server.apps.investment_object.api.serializers import TenderLotSerializer
from server.apps.investment_object.models import TenderLot
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class TenderLotFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр лотов тендеров."""

    class Meta:
        model = TenderLot
        fields = (
            'id',
            'tender_lot_id',
            'name',
            'url',
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

