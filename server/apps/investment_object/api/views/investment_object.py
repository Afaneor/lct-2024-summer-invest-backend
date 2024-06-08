import django_filters
from django.db import models
from rest_framework.decorators import action

from server.apps.investment_object.api.serializers import (
    InvestmentObjectSerializer,
)
from server.apps.investment_object.models import InvestmentObject
from server.apps.services.filters_mixins import CreatedUpdatedDateFilterMixin
from server.apps.services.views import RetrieveListCreateViewSet


class InvestmentObjectFilter(
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр инвестиционных площадок."""

    economic_activity = django_filters.CharFilter(
        method='filter_economic_activity',
        label='Фильтрация по экономической деятельности',
    )
    preferential_treatment = django_filters.CharFilter(
        method='filter_preferential_treatment',
        label='Фильтрация по преференциальному режиму',
    )

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'object_type',
            'economic_activity',
        )

    def filter_economic_activity(self, queryset, name, value):
        """Фильтрация по экономической деятельности."""
        return queryset.filter(
            models.Q(specialized_site__economic_activities__name__icontains=value) |
            models.Q(real_estate__economic_activities__name__icontains=value)
        )

    def filter_preferential_treatment(self, queryset, name, value):
        """Фильтрация по преференциальному режиму"""
        return queryset.filter(
            models.Q(real_estate__preferential_treatment__icontains=value)
        )


class InvestmentObjectViewSet(RetrieveListCreateViewSet):
    """Инвестиционные площадки."""

    serializer_class = InvestmentObjectSerializer
    queryset = InvestmentObject.objects.all()
    search_fields = (
        'external_id',
        'name',
    )
    ordering_fields = '__all__'
    filterset_class = InvestmentObjectFilter

    # @action(
    #     methods=['GET'],
    #     url_path='data-for-filters',
    #     detail=False,
    #     serializer_class=SelectionRequestSerializer,
    # )
    # def data_for_filters(
    #     self,
    #     request: Request,
    # ):
    #     """
    #     Получение актуального запроса на подбор площадок.
    #     """
    #     if request.user.is_authenticated:
    #         actual_selection_request, created = SelectionRequest.objects.get_or_create(
    #             is_actual=True,
    #             user=request.user,
    #         )
    #
    #     else:
    #         generate_user_id = self.request.headers.get('GENERATED-USER-ID')
    #         actual_selection_request, created = SelectionRequest.objects.get_or_create(
    #             is_actual=True,
    #             anonymous_user_id=generate_user_id,
    #         )
    #
    #     serializer = self.get_serializer(actual_selection_request)
    #     return Response(
    #         data=serializer.data,
    #         status=status.HTTP_200_OK,
    #     )
