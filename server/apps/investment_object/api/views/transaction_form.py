import django_filters

from server.apps.investment_object.api.serializers import (
    TransactionFormSerializer,
)
from server.apps.investment_object.models import TransactionForm
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet


class TransactionFormFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр формы сделки."""

    class Meta:
        model = TransactionForm
        fields = (
            'id',
            'name',
            'transaction_form_type',
        )


class TransactionFormViewSet(RetrieveListViewSet):
    """Лот тендера."""

    serializer_class = TransactionFormSerializer
    queryset = TransactionForm.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = TransactionFormFilter

