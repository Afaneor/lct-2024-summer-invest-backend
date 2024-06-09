import django_filters
from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.investment_object.api.serializers import (
    DetailInvestmentObjectSerializer, UploadDataFromFileSerializer, ListInvestmentObjectSerializer,
)
from server.apps.investment_object.models import (
    EconomicActivity,
    InvestmentObject,
    RealEstate,
)
from server.apps.investment_object.tasks import delayed_parsing_data
from server.apps.services.enums import UploadDataFromFileType
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.parsing.xlsx.real_estate import parsing_real_estate
from server.apps.services.parsing.xlsx.specialized_site import \
    parsing_specialized_site
from server.apps.services.views import RetrieveListCreateViewSet
from django.utils.translation import gettext_lazy as _


class InvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    economic_activity_name = django_filters.CharFilter(
        method='filter_economic_activity_name',
        label='Фильтрация по экономической деятельности',
    )
    preferential_treatment = django_filters.MultipleChoiceFilter(
        method='filter_preferential_treatment',
        label='Фильтрация по преференциальному режиму',
    )
    transaction_form_name = django_filters.MultipleChoiceFilter(
        method='filter_transaction_form_name',
        label='Фильтрация по форме сделки',
    )
    from_cost = django_filters.NumberFilter(
        method='filter_form_cost',
        label='Фильтрация по форме сделки',
    )
    to_cost = django_filters.NumberFilter(
        method='filter_to_cost',
        label='Фильтрация по форме сделки',
    )
    municipality = django_filters.MultipleChoiceFilter(
        method='filter_municipality',
        label='Фильтрация муниципальному образованию',
    )
    # Дополнительные фильтры, которые относятся непосредственно к
    # определенным объектам
    infrastructure = django_filters.MultipleChoiceFilter(
        method='filter_infrastructure',
        label='Фильтрация по инфраструктуре',
    )

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'object_type',
            'economic_activity_name',
            'preferential_treatment',
            'transaction_form_name',
            'from_cost',
            'to_cost',
            'municipality',
        )

    def filter_economic_activity_name(self, queryset, name, values):
        """Фильтрация по названию экономической деятельности."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(specialized_site__economic_activities__name__icontains=value) |
                models.Q(real_estate__economic_activities__name__icontains=value)
            )
        return queryset.filter(filters)

    def filter_preferential_treatment(self, queryset, name, values):
        """Фильтрация по преференциальному режиму."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(real_estate__preferential_treatment__icontains=value)
            )
        return queryset.filter(filters)

    def filter_transaction_form_name(self, queryset, name, values):
        """Фильтрация по форме сделки."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(real_estate__transaction_form__name__icontains=value) |
                models.Q(tender_lot__transaction_form__name__icontains=value) |
                models.Q(specialized_site__transaction_form__name__icontains=value) |
                models.Q(ready_business__transaction_form__name__icontains=value)
            )
        return queryset.filter(filters)

    def filter_form_cost(self, queryset, name, values):
        """Фильтрация стоимости."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(real_estate__cost__gte=value) |
                models.Q(tender_lot__cost__gte=value) |
                models.Q(specialized_site__cost__gte=value) |
                models.Q(ready_business__cost__gte=value)
            )
        return queryset.filter(filters)

    def filter_to_cost(self, queryset, name, values):
        """Фильтрация стоимости."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(real_estate__cost__lte=value) |
                models.Q(tender_lot__cost__lte=value) |
                models.Q(specialized_site__cost__lte=value) |
                models.Q(ready_business__cost__lte=value)
            )
        return queryset.filter(filters)

    def filter_municipality(self, queryset, name, values):
        """Фильтрация по муниципальному образованию."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(real_estate__municipality__icontains=value) |
                models.Q(tender_lot__municipality__icontains=value) |
                models.Q(specialized_site__municipality__icontains=value) |
                models.Q(ready_business__municipality__icontains=value)
            )
        return queryset.filter(filters)

    def filter_infrastructure(self, queryset, name, values):
        """Фильтрация по инфраструктуре."""
        filters = models.Q()
        for value in values.split(';'):
            filters |= models.Q(
                models.Q(real_estate__infrastructures__name__icontains=value) |
                models.Q(specialized_site__infrastructures__name__icontains=value)
            )
        return queryset.filter(filters)


class InvestmentObjectViewSet(RetrieveListCreateViewSet):
    """Инвестиционные площадки."""

    serializer_class = DetailInvestmentObjectSerializer
    list_serializer_class = ListInvestmentObjectSerializer
    queryset = InvestmentObject.objects.all()
    search_fields = (
        'external_id',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InvestmentObjectFilter
    permission_type_map = {
        **RetrieveListCreateViewSet.permission_type_map,
        'data_for_filters': 'view',
        'add_data_from_xlsx_file': 'action_is_superuser',
    }

    @action(
        methods=['GET'],
        url_path='data-for-filters',
        detail=False,
    )
    def data_for_filters(
        self,
        request: Request,
    ):
        """
        Получение данных для фильтров.
        """
        filters = {
            'economic_activity_name': EconomicActivity.objects.values_list(
                'name',
                flat=True,
            ),
            'preferential_treatment': RealEstate.objects.order_by(
                'preferential_treatment',
            ).distinct(
                'preferential_treatment',
            ).values_list(
                'preferential_treatment',
                flat=True,
            ),
            'transaction_form': RealEstate.objects.order_by(
                'transaction_form',
            ).distinct(
                'transaction_form',
            ).values_list(
                'transaction_form',
                flat=True,
            ),
        }
        return Response(
            data=filters,
            status=status.HTTP_200_OK,
        )

    @action(  # type: ignore
        methods=['POST'],
        url_path='add-data-from-xlsx-file',
        detail=False,
        serializer_class=UploadDataFromFileSerializer,
    )
    def add_data_from_xlsx_file(self, request: Request):
        """Загрузка данных из xlsx файла."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with request.FILES['file'].open(mode='r') as file:
            delayed_parsing_data.apply_async(
                kwargs={
                    'file': file,
                    'object_type': serializer.validated_data['object_type'],
                },
            ),

        return Response(
            data={'detail': _('Данные загружены. Происходит их обработка')},
            status=status.HTTP_201_CREATED
        )
