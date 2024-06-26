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
    InvestmentObject,
    RealEstate,
    SpecializedSite,
    TransactionForm,
)
from server.apps.investment_object.tasks import delayed_parsing_data
from server.apps.services.enums import ObjectType, TransactionFormType
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    NonValidatingMultipleChoiceFilter,
)
from server.apps.services.views import RetrieveListCreateViewSet


class InvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    id = NonValidatingMultipleChoiceFilter(
        label=_('Фильтрация id объекта'),
    )
    economic_activity_name = NonValidatingMultipleChoiceFilter(
        field_name='economic_activities__name',
        label=_('Фильтрация по названию экономической деятельности'),
    )
    economic_activity_code = NonValidatingMultipleChoiceFilter(
        field_name='economic_activities__code',
        label=_('Фильтрация по коду экономической деятельности'),
    )
    preferential_treatment = NonValidatingMultipleChoiceFilter(
        field_name='real_estate__preferential_treatment',
        label=_('Фильтрация по преференциальному режиму'),
    )
    transaction_form_name = NonValidatingMultipleChoiceFilter(
        field_name='transaction_form__name',
        label=_('Фильтрация по названию формы сделки'),
    )
    transaction_form_type = NonValidatingMultipleChoiceFilter(
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
    location = NonValidatingMultipleChoiceFilter(
        label=_('Фильтрация по местоположению'),
    )
    site_type = NonValidatingMultipleChoiceFilter(
        field_name='real_estate__site_type',
        label=_('Фильтрация по типу площадки'),
    )
    specialized_site_is_free_customs_zone_regime = NonValidatingMultipleChoiceFilter(
        field_name='specialized_site__is_free_customs_zone_regime',
        label=_('Фильтрация по наличию режима свободной таможенной зоны'),
    )
    real_estate_maip = NonValidatingMultipleChoiceFilter(
        field_name='real_estate__maip',
        label=_('Фильтрация по наличию МАИП'),
        lookup_expr='icontains',
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
            'data_source',
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
    ).order_by('id')
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InvestmentObjectFilter
    permission_type_map = {
        **RetrieveListCreateViewSet.permission_type_map,
        'additional_data': 'view',
        'add_data_from_xlsx_file': 'action_is_superuser',
    }

    @action(
        methods=['GET'],
        url_path='additional-data',
        detail=False,
    )
    def additional_data(
        self,
        request: Request,
    ):
        """
        Получение данных для фильтров.
        """
        filters = {
            'object_type': dict(ObjectType.choices),
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
