import django_filters
from rest_framework.decorators import action
from rest_framework.request import Request

from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import BaseReadOnlyViewSet
from server.apps.support.api.serializers import (
    DetailServiceSupportSerializer,
    ListServiceSupportSerializer,
)
from server.apps.support.models import ServiceSupport
from django.utils.translation import gettext_lazy as _


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
    is_msp_roster = django_filters.AllValuesMultipleFilter(
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
            'is_msp_roster',
            'economic_activities_name',
        )


class ServiceSupportViewSet(BaseReadOnlyViewSet):
    """Инфраструктура."""

    serializer_class = DetailServiceSupportSerializer
    list_serializer_class = ListServiceSupportSerializer
    queryset = ServiceSupport.objects.all()
    search_fields = (
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = ServiceSupportFilter
    # permission_type_map = {
    #     **BaseReadOnlyViewSet.permission_type_map,
    #     'data_for_filters': 'view',
    # }
    #
    # @action(
    #     methods=['GET'],
    #     url_path='data-for-filters',
    #     detail=False,
    # )
    # def data_for_filters(
    #     self,
    #     request: Request,
    # ):
    #     """
    #     Получение данных для фильтров.
    #     """
    #     filters = {
    #         'support_type': ServiceSupport.objects.order_by(
    #             'support_type',
    #         ).distinct(
    #             'support_type',
    #         ).values_list(
    #             'support_type',
    #             flat=True,
    #         ),
    #         'support_level': ServiceSupport.objects.order_by(
    #             'support_level',
    #         ).distinct(
    #             'support_level',
    #         ).values_list(
    #             'support_level',
    #             flat=True,
    #         ),
    #         'is_msp_roster': ServiceSupport.objects.order_by(
    #             'is_msp_roster',
    #         ).distinct(
    #             'is_msp_roster',
    #         ).values_list(
    #             'is_msp_roster',
    #             flat=True,
    #         ),
    #         'is_msp_roster': ServiceSupport.objects.order_by(
    #             'is_msp_roster',
    #         ).distinct(
    #             'is_msp_roster',
    #         ).values_list(
    #             'is_msp_roster',
    #             flat=True,
    #         ),
    #     }
    #     return Response(
    #         data=filters,
    #         status=status.HTTP_200_OK,
    #     )
