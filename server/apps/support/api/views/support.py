import django_filters

from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    TagFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet
from server.apps.support.api.serializers import SupportSerializer
from server.apps.support.models import Support


class SupportFilter(
    TagFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр мер поддержки."""

    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Support
        fields = (
            'title',
            'tags',
            'is_actual',
        )


class SupportViewSet(BaseReadOnlyViewSet):
    """Меры поддержки. Просмотр."""

    serializer_class = SupportSerializer
    queryset = Support.objects.prefetch_related('tags')
    ordering_fields = '__all__'
    search_fields = ('title',)
    filterset_class = SupportFilter

    def get_queryset(self):  # noqa: WPS615
        """Выдача мер поддержки.

        Суперпользователь видит все.
        Остальные видят только актуальные меры.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        return queryset.filter(is_actual=True)
