import django_filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.personal_cabinet.api.serializers import (
    CreateMessageSerializer,
    MessageSerializer,
)
from server.apps.personal_cabinet.models.message import Message
from server.apps.personal_cabinet.models.selection_request import (
    SelectionRequest,
)
from server.apps.personal_cabinet.services.send_data_in_chat_gpt import (
    send_data_in_chat_gpt,
)
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateViewSet
from server.apps.user.models import User


class MessageFilter(
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
    django_filters.FilterSet,
):
    """
    Фильтр отраслей.
    """

    user = django_filters.ModelMultipleChoiceFilter(
        field_name='selection_request__user',
        queryset=User.objects.all(),
    )
    user_email = django_filters.CharFilter(
        field_name='selection_request__user__email',
        lookup_expr='icontains',
    )
    user_username = django_filters.CharFilter(
        field_name='selection_request__user__username',
        lookup_expr='icontains',
    )
    user_first_name = django_filters.CharFilter(
        field_name='selection_request__user__first_name',
        lookup_expr='icontains',
    )
    user_last_name = django_filters.CharFilter(
        field_name='selection_request__user__last_name',
        lookup_expr='icontains',
    )
    user_middle_name = django_filters.CharFilter(
        field_name='selection_request__user__middle_name',
        lookup_expr='icontains',
    )
    text = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Message
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'selection_request',
            'owner_type',
            'text',
        )


class MessageViewSet(RetrieveListCreateViewSet):
    """
    Сообщение. Просмотр/добавление.
    """

    serializer_class = MessageSerializer
    create_serializer_class = CreateMessageSerializer
    queryset = Message.objects.all()
    search_fields = (
        'selection_request__user__email',
        'selection_request__user__first_name',
        'selection_request__user_last_name',
    )
    ordering_fields = '__all__'
    filterset_class = MessageFilter

    def perform_create(self, serializer):
        """
        Сохраняем сообщение от пользователя и отправляем данные в ChatGpt.
        """
        serializer.save()
        send_data_in_chat_gpt(
            user_text=serializer.validated_data['text'],
            message_id=serializer.instance.id,
            selection_request_id=serializer.instance.selection_request.id,
        )

    def get_queryset(self):
        """
        Выдача сообщений.

        Сообщение видит только владелец.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        if user.is_authenticated:
            return queryset.filter(
                selection_request__in=user.selection_requests,
            )

        selection_requests = SelectionRequest.objects.filter(
            anonymous_user_id=self.request.headers.get('GENERATED-USER-ID')
        )
        return queryset.filter(selection_request__in=selection_requests)
