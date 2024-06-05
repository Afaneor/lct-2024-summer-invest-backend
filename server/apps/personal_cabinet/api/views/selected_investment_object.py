import django_filters

from server.apps.personal_cabinet.api.serializers import (
    SelectedInvestmentObjectSerializer,
)
from server.apps.personal_cabinet.models import SelectedInvestmentObject
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListUpdateViewSet


class SelectedInvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """
    Фильтр подобранного инвестиционного объекта.
    """

    class Meta:
        model = SelectedInvestmentObject
        fields = (
            'id',
            'investment_object',
            'selection_request',
            'message',
            'is_relevant',
        )


class SelectedInvestmentObjectViewSet(RetrieveListUpdateViewSet):
    """Подобранный инвестиционный объект. Просмотр/изменение."""

    serializer_class = SelectedInvestmentObjectSerializer
    queryset = SelectedInvestmentObject.objects.all()
    search_fields = (
        'investment_object__name',
        'selection_request__user',
    )
    ordering_fields = '__all__'
    filterset_class = SelectedInvestmentObjectFilter

    def get_queryset(self):
        """Выдача подотраслей.

        Все видят все подотрасли.
        """
        return super().get_queryset()
