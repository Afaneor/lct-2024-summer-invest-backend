import django_filters
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.investment_object.models import EconomicActivity
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListViewSet
from server.apps.support.api.serializers import (
    DetailServiceSupportSerializer,
    ListServiceSupportSerializer,
)
from server.apps.support.models import ServiceSupport


class ServiceSupportFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инфраструктуры."""

    support_type = django_filters.AllValuesMultipleFilter(
        label=_('Фильтрация по типу поддержки'),
    )
    support_level = django_filters.AllValuesMultipleFilter(
        label=_('Фильтрация по уровню поддержки'),
    )
    msp_roster = django_filters.AllValuesMultipleFilter(
        label=_('Фильтрация по требованию вхождения в реестр МСП'),
    )
    economic_activities_name = django_filters.AllValuesMultipleFilter(
        field_name='economic_activities__name',
        label=_('Фильтрация по экономической деятельности'),
    )

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
            'name',
            'support_type',
            'support_level',
            'msp_roster',
            'economic_activities_name',
        )


class ServiceSupportViewSet(RetrieveListViewSet):
    """Инфраструктура."""

    serializer_class = DetailServiceSupportSerializer
    list_serializer_class = ListServiceSupportSerializer
    queryset = ServiceSupport.objects.prefetch_related(
        'economic_activities',
        'restrictions',
    )
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ServiceSupportFilter
    permission_type_map = {
        **RetrieveListViewSet.permission_type_map,
        'data_for_filters': 'view',
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
            'support_type': ServiceSupport.objects.all().order_by(
                'support_type',
            ).distinct(
                'support_type',
            ).values_list(
                'support_type',
                flat=True,
            ),
            'support_level': ServiceSupport.objects.all().order_by(
                'support_level',
            ).distinct(
                'support_level',
            ).values_list(
                'support_level',
                flat=True,
            ),
            'msp_roster': ServiceSupport.objects.all().order_by(
                'msp_roster',
            ).distinct(
                'msp_roster',
            ).values_list(
                'msp_roster',
                flat=True,
            ),
            'economic_activity_name': EconomicActivity.objects.values_list(
                'name',
                flat=True,
            ),
        }
        return Response(
            data=filters,
            status=status.HTTP_200_OK,
        )
