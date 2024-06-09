import django_filters
from rest_framework import status
from rest_framework.response import Response

from server.apps.personal_cabinet.api.serializers import (
    CreateSubscriptionSerializer,
    SubscriptionSerializer,
    UpdateSubscriptionSerializer,
)
from server.apps.personal_cabinet.models import Subscription
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

    def create(self, request, *args, **kwargs):
        """Создание подписки на объекты системы."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.instance, created = Subscription.objects.get_or_create(
            user=request.user,
            subscription_type=serializer.validated_data['subscription_type'],
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
