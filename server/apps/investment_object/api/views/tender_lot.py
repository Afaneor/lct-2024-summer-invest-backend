import django_filters

from server.apps.investment_object.api.serializers import TenderLotSerializer
from server.apps.investment_object.models import TenderLot
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class TenderLotFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр лотов тендеров."""

    class Meta:
        model = TenderLot
        fields = (
            'id',
            'investment_object',
        )


class TenderLotViewSet(RetrieveListViewSet):
    """Лот тендера."""

    serializer_class = TenderLotSerializer
    queryset = TenderLot.objects.all()
    search_fields = (
        'investment_object__name',
    )
    ordering_fields = '__all__'
    filterset_class = TenderLotFilter

