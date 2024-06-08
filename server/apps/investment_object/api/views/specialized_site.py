import django_filters

from server.apps.investment_object.api.serializers import (
    SpecializedSiteSerializer,
)
from server.apps.investment_object.models import SpecializedSite
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet


class SpecializedSiteFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр ограничений по видам деятельности."""

    class Meta:
        model = SpecializedSite
        fields = (
            'id',
        )


class SpecializedSiteViewSet(BaseReadOnlyViewSet):
    """Ограничения по видам деятельности."""

    serializer_class = SpecializedSiteSerializer
    queryset = SpecializedSite.objects.all()
    search_fields = (
        'id',
    )
    ordering_fields = '__all__'
    filterset_class = SpecializedSiteFilter
