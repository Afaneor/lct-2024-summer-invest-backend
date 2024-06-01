import django_filters

from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    TagFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet
from server.apps.support.api.serializers import OfferSerializer
from server.apps.support.models import Offer


class OfferFilter(
    TagFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр партнерских предложений."""

    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Offer
        fields = (
            'title',
            'tags',
        )


class OfferViewSet(BaseReadOnlyViewSet):
    """Партнерские предложения. Просмотр."""

    serializer_class = OfferSerializer
    queryset = Offer.objects.prefetch_related('tags')
    ordering_fields = '__all__'
    search_fields = ('title',)
    filterset_class = OfferFilter

    def get_queryset(self):  # noqa: WPS615
        """Выдача партнерских предложений.

        Суперпользователь видит все.
        Остальные видят только актуальные меры.
        """
        return super().get_queryset()
