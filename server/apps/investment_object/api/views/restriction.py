import django_filters

from server.apps.investment_object.api.serializers import RestrictionSerializer
from server.apps.investment_object.models import Restriction
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class RestrictionFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр ограничений по видам деятельности."""

    class Meta:
        model = Restriction
        fields = (
            'id',
            'name',
        )


class RestrictionViewSet(BaseReadOnlyViewSet):
    """Ограничения по видам деятельности."""

    serializer_class = RestrictionSerializer
    queryset = Restriction.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = RestrictionFilter
