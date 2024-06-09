import django_filters

from server.apps.investment_object.api.serializers import PrivilegeSerializer
from server.apps.investment_object.models import Privilege
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class PrivilegeFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр льгот."""

    class Meta:
        model = Privilege
        fields = (
            'id',
            'name',
        )


class PrivilegeViewSet(RetrieveListViewSet):
    """Льгота."""

    serializer_class = PrivilegeSerializer
    queryset = Privilege.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = PrivilegeFilter
