import django_filters
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.investment_object.api.serializers import (
    DetailInvestmentObjectSerializer,
    ListInvestmentObjectSerializer,
    UploadDataFromFileSerializer,
)
from server.apps.investment_object.models import (
    EconomicActivity,
    InvestmentObject,
    RealEstate, SpecializedSite, TransactionForm,
)
from server.apps.investment_object.tasks import delayed_parsing_data
from server.apps.personal_cabinet.models import SelectedEntity
from server.apps.services.enums import TransactionFormType, ObjectType
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListCreateViewSet


class InvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    economic_activity_name = django_filters.AllValuesMultipleFilter(
        field_name='economic_activities__name',
        label=_('Фильтрация по экономической деятельности'),
    )
    preferential_treatment = django_filters.AllValuesMultipleFilter(
        field_name='real_estate__preferential_treatment',
        label=_('Фильтрация по преференциальному режиму'),
    )
    transaction_form_name = django_filters.MultipleChoiceFilter(
        field_name='transaction_form__name',
        label=_('Фильтрация по названию формы сделки'),
    )
    transaction_form_type = django_filters.MultipleChoiceFilter(
        field_name='transaction_form__transaction_form_type',
        label=_('Фильтрация по типу формы сделки'),
    )
    cost = django_filters.NumericRangeFilter(
        label=_('Фильтрация по стоимости'),
    )
    land_area = django_filters.NumberFilter(
        label=_('Фильтрация по площади земли'),
    )
    building_area = django_filters.NumberFilter(
        label=_('Фильтрация по площади помещения'),
    )
    location = django_filters.AllValuesMultipleFilter(
        label=_('Фильтрация по местоположению'),
    )
    site_type = django_filters.MultipleChoiceFilter(
        field_name='real_estate__site_type',
        label=_('Фильтрация по типу площадки'),
    )
    specialized_site_is_free_customs_zone_regime = django_filters.MultipleChoiceFilter(
        field_name='specialized_site__is_free_customs_zone_regime',
        label=_('Фильтрация по наличию режима свободной таможенной зоны'),
    )
    real_estate_maip = django_filters.MultipleChoiceFilter(
        field_name='real_estate__maip',
        label=_('Фильтрация по наличию МАИП'),
    )

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'object_type',
            'economic_activity_name',
            'preferential_treatment',
            'transaction_form',
            'transaction_form_name',
            'transaction_form_type',
            'land_area',
            'building_area',
            'location',
            'site_type',
            'specialized_site_is_free_customs_zone_regime',
            'real_estate_maip',
        )


class InvestmentObjectViewSet(RetrieveListCreateViewSet):
    """Инвестиционные площадки."""

    serializer_class = DetailInvestmentObjectSerializer
    list_serializer_class = ListInvestmentObjectSerializer
    queryset = InvestmentObject.objects.select_related(
        'ready_business',
        'tender_lot',
        'specialized_site',
        'real_estate',
        'transaction_form',
    ).prefetch_related(
        'economic_activities',
    )
    search_fields = (
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
            'object_type': ObjectType.labels,
            'economic_activity_name': EconomicActivity.objects.order_by(
                'name',
            ).distinct(
                'name',
            ).values_list(
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
            'transaction_form_name': TransactionForm.objects.order_by(
                'name',
            ).distinct(
                'name',
            ).values_list(
                'name',
                flat=True,
            ),
            'transaction_form_type': TransactionFormType.labels,
            'location': InvestmentObject.objects.order_by(
                'location',
            ).distinct(
                'location',
            ).values_list(
                'location',
                flat=True,
            ),
            'site_type': RealEstate.objects.order_by(
                'site_type',
            ).distinct(
                'site_type',
            ).values_list(
                'site_type',
                flat=True,
            ),
            'specialized_site_is_free_customs_zone_regime': (
                SpecializedSite.objects.order_by(
                    'is_free_customs_zone_regime',
                ).distinct(
                    'is_free_customs_zone_regime',
                ).values_list(
                    'is_free_customs_zone_regime',
                    flat=True,
                )
            ),
            'real_estate_maip': RealEstate.objects.order_by(
                'maip',
            ).distinct(
                'maip',
            ).values_list(
                'maip',
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

    @action(  # type: ignore
        methods=['POST'],
        url_path='statistics',
        detail=False,
    )
    def statistics(self, request: Request):
        """Статистика по всему порталу."""
        return {
            # Какими объектами как часто интересуются.
            'investment_object_type': SelectedEntity.objects.values(
                investment_object_type=models.F(
                    'investment_object__object_type',
                ),
            ).annotate(count=models.Count('id')).order_by('count')[10],
            # Какими мерами поддержки как часто интересуются.
            'service_support_type': SelectedEntity.objects.values(
                service_support_type=models.F(
                    'service_support__name',
                ),
            ).annotate(count=models.Count('id')).order_by('count')[10],
            # Какие проблемы чаще всего возникают.
            'problem_type': SelectedEntity.objects.values(
                problem_type=models.F(
                    'problem___theme',
                ),
            ).annotate(count=models.Count('id')).order_by('count')[10],
        }
