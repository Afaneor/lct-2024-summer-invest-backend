import django_filters

from server.apps.personal_cabinet.api.serializers import (
    SelectedEntitySerializer,
)
from server.apps.personal_cabinet.models import SelectedEntity
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListUpdateViewSet


class SelectedEntityFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """
    Фильтр подобранного инвестиционного объекта.
    """

    class Meta:
        model = SelectedEntity
        fields = (
            'id',
            'investment_object',
            'selection_request',
            'message',
            'is_relevant',
        )


class SelectedEntityViewSet(RetrieveListUpdateViewSet):
    """Подобранный инвестиционный объект. Просмотр/изменение."""

    serializer_class = SelectedEntitySerializer
    queryset = SelectedEntity.objects.all()
    search_fields = (
        'investment_object__name',
        'selection_request__user',
    )
    ordering_fields = '__all__'
    filterset_class = SelectedEntityFilter

    def get_queryset(self):
        """Выдача подотраслей.

        Все видят все подотрасли.
        """
        return super().get_queryset()
