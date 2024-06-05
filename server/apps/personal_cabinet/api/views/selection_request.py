import django_filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.personal_cabinet.api.serializers import (
    CreateSelectionRequestSerializer,
    SelectionRequestSerializer,
)
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateViewSet


class SelectionRequestFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр запроса на подбор."""

    name = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SelectionRequest
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'anonymous_user_id',
            'is_actual',
        )


class SelectionRequestViewSet(RetrieveListCreateViewSet):
    """
    Запрос на подбор. Просмотр/создание.
    """

    serializer_class = SelectionRequestSerializer
    create_serializer_class = CreateSelectionRequestSerializer
    queryset = SelectionRequest.objects.select_related('user').prefetch_related('investment_objects')
    search_fields = (
        'user__email',
        'user__first_name',
        'user_last_name',
        'anonymous_user_id',
    )
    ordering_fields = '__all__'
    filterset_class = SelectionRequestFilter
    permission_type_map = {
        **RetrieveListCreateViewSet.permission_type_map,
        'actual': 'view',
        'completed': 'add',
    }

    def perform_create(self, serializer):
        """
        Добавляем информацию о пользователе.

        Перевод ранее активного запроса в выполненный.
        """
        serializer.validated_data.update(user=self.request.user)
        SelectionRequest.objects.filter(
            is_actual=True,
        ).update(
            is_actual=False,
        )
        serializer.save()

    def get_queryset(self):
        """
        Выдача подотраслей.

        Все видят все подотрасли.
        """
        return super().get_queryset()

    @action(
        methods=['GET'],
        url_path='actual',
        detail=False,
        serializer_class=SelectionRequestSerializer,
    )
    def actual(
        self,
        request: Request,
    ):
        """
        Получение актуального запроса на подбор площадок.
        """
        actual_selection_request = SelectionRequest.objects.filter(
            is_actual=True,
        )
        if actual_selection_request.exists():
            serializer = self.get_serializer(actual_selection_request.first())
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(
            data={'detail': 'Здравствуйте! Я помогу вам с подбором инвестиционных площадок!'},
            status=status.HTTP_200_OK,
        )

    @action(
        methods=['POST'],
        url_path='completed',
        detail=False,
        serializer_class=SelectionRequestSerializer,
    )
    def completed(
        self,
        request: Request,
    ):
        """
        Завершить запрос на подбор площадок.
        """
        SelectionRequest.objects.filter(
            is_actual=True,
        ).update(
            is_actual=False,
        )
        return Response(
            data={'detail': 'Если появятся вопросы, вы знаете где меня найти!'},
            status=status.HTTP_200_OK,
        )
