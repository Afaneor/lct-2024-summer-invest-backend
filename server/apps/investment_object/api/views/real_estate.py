import django_filters

from server.apps.investment_object.api.serializers import RealEstateSerializer
from server.apps.investment_object.models import RealEstate
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class RealEstateFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр недвижимости"""

    class Meta:
        model = RealEstate
        fields = (
            'id',
            'investment_object',
        )


class RealEstateViewSet(RetrieveListViewSet):
    """Недвижимость."""

    serializer_class = RealEstateSerializer
    queryset = RealEstate.objects.all()
    search_fields = (
        'investment_object__name',
    )
    ordering_fields = '__all__'
    filterset_class = RealEstateFilter
