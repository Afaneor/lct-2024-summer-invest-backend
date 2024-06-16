import time

import django_filters
from django.http import FileResponse
from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.personal_cabinet.api.serializers import (
    CreateSelectionRequestSerializer,
    SelectionRequestSerializer,
)
from server.apps.personal_cabinet.models import SelectionRequest
from server.apps.personal_cabinet.services.report_file import (
    SelectionRequestFile,
)
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
    queryset = SelectionRequest.objects.select_related(
        'user',
    ).prefetch_related(
        'messages',
    )
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
        'check_message_from_bot': 'view',
        'download': 'view',
    }

    def perform_create(self, serializer):
        """
        Добавляем информацию о пользователе.

        Перевод ранее активного запроса в выполненный.
        """
        if self.request.user.is_authenticated:
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
        if request.user.is_authenticated:
            actual_selection_request, created = SelectionRequest.objects.get_or_create(
                is_actual=True,
                user=request.user,
            )

        else:
            generate_user_id = self.request.headers.get('GENERATED-USER-ID')
            actual_selection_request, created = SelectionRequest.objects.get_or_create(
                is_actual=True,
                anonymous_user_id=generate_user_id if generate_user_id else '',
            )

        serializer = self.get_serializer(actual_selection_request)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    @action(
        methods=['POST'],
        url_path='completed',
        detail=False,
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
        return Response(status=status.HTTP_200_OK)

    @action(
        methods=['GET'],
        url_path='check-message-from-bot',
        detail=False,
    )
    def check_message_from_bot(
        self,
        request: Request,
    ):
        """
        Ожидает ли запрос на подбор ответа от чат-бота или нет.
        """
        try:
            selection_requests = SelectionRequest.objects.get(
                is_actual=True
            )
            return Response(
                data={
                    'is_bot_response_waiting':
                        selection_requests.is_bot_response_waiting,
                },
                status=status.HTTP_200_OK,
            )

        except SelectionRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(
        methods=['POST'],
        url_path='download',
        detail=True,
    )
    def download(
        self,
        request: Request,
        pk: int
    ):
        """
        Скачать отчет в формате pdf.
        """
        instance = self.get_object()
        if request.user.is_authenticated:
            selection_request_file = SelectionRequestFile(
                document_format='docx',
                selection_request=instance,
            )

            return FileResponse(
                selection_request_file.generate(),
                content_type='application/pdf',
                filename=selection_request_file.get_file_name(),
                status=status.HTTP_200_OK,
            )
        return Response(status=status.HTTP_403_FORBIDDEN)
