import django_filters

from server.apps.hincal.api.serializers import ArchiveSerializer
from server.apps.hincal.models import Archive
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import BaseReadOnlyViewSet


class ArchiveFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр архивов."""

    year = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Archive
        fields = (
            'id',
            'year',
            'is_actual',
        )


class ArchiveViewSet(BaseReadOnlyViewSet):
    """Архив. Просмотр."""

    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()
    search_fields = (
        'year',
    )
    ordering_fields = '__all__'
    filterset_class = ArchiveFilter

    def get_queryset(self):
        """Выдача архивов.

        Суперпользователь видит все.
        Остальные видят только актуальный.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        return queryset.filter(is_actual=True)
