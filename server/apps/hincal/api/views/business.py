import django_filters
from rest_framework.viewsets import ModelViewSet

from server.apps.hincal.api.serializers import BusinessSerializer
from server.apps.hincal.models import Business
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import BaseModelViewSet


class BusinessFilter(
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр бизнеса."""

    short_business_name = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    site = django_filters.CharFilter(lookup_expr='icontains')

    class Meta(object):
        model = Business
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'type',
            'inn',
            'sector',
            'sub_sector',
            'territorial_location',
            'short_business_name',
            'address',
            'email',
            'site',
        )


class BusinessViewSet(BaseModelViewSet):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    search_fields = (
        'user_email',
        'user_username',
        'user_first_name',
        'user_last_name',
        'user_middle_name',
        'short_business_name',
        'address',
    )
    ordering_fields = '__all__'
    filterset_class = BusinessFilter

    def get_queryset(self):
        """Выдача бизнеса.

        Суперпользователь видит все бизнесы.
        Остальные видят свой бизнес.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        if user.is_anonymous:
            return queryset.none()

        return queryset.filter(user=user)
