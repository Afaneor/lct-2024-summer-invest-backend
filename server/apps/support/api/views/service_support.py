import django_filters
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    NonValidatingMultipleChoiceFilter,
)
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

    support_type = NonValidatingMultipleChoiceFilter(
        label=_('Фильтрация по типу поддержки'),
    )
    support_level = NonValidatingMultipleChoiceFilter(
        label=_('Фильтрация по уровню поддержки'),
    )
    msp_roster = NonValidatingMultipleChoiceFilter(
        label=_('Фильтрация по требованию вхождения в реестр МСП'),
    )
    economic_activity_name = NonValidatingMultipleChoiceFilter(
        field_name='economic_activities__name',
        label=_('Фильтрация по названию экономической деятельности'),
    )
    economic_activity_code = NonValidatingMultipleChoiceFilter(
        field_name='economic_activities__code',
        label=_('Фильтрация по коду экономической деятельности'),
    )

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
            'name',
            'support_type',
            'support_level',
            'msp_roster',
            'economic_activity_name',
            'economic_activity_code',
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
        'additional_data': 'view',
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
        }
        return Response(
            data=filters,
            status=status.HTTP_200_OK,
        )
