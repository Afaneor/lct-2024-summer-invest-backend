import django_filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.personal_cabinet.api.serializers import (
    CreateSubscriptionSerializer,
    SubscriptionSerializer,
    UpdateSubscriptionSerializer,
)
from server.apps.personal_cabinet.models import Subscription
from server.apps.services.enums import SubscriptionType
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateDeleteViewSet


class SubscriptionFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр подписки."""

    class Meta:
        model = Subscription
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'subscription_type',
        )


class SubscriptionViewSet(RetrieveListCreateDeleteViewSet):
    """Подписка. Просмотр/удаление."""

    serializer_class = SubscriptionSerializer
    create_serializer_class = CreateSubscriptionSerializer
    update_serializer_class = UpdateSubscriptionSerializer
    queryset = Subscription.objects.all()
    search_fields = (
        'subscription_type',
    )
    ordering_fields = '__all__'
    filterset_class = SubscriptionFilter
    permission_type_map = {
        **RetrieveListCreateDeleteViewSet.permission_type_map,
        'data_for_filters': 'view',
    }

    def create(self, request, *args, **kwargs):
        """Создание подписки на объекты системы."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.instance, created = Subscription.objects.update_or_create(
            user=request.user,
            subscription_type=serializer.validated_data['subscription_type'],
            defaults={
                'email': serializer.validated_data['email'],
                'telegram_username':
                    serializer.validated_data.get('telegram_username'),
            },
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        """Выдача подписок. Видны только свои подписки.

        Все видят все подотрасли.
        """
        queryset = super().get_queryset()
        user = self.request.user

        return queryset.filter(user=user)

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
            'subscription_type': dict(SubscriptionType.choices),
        }
        return Response(
            data=filters,
            status=status.HTTP_200_OK,
        )
