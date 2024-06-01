import django_filters
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from server.apps.hincal.api.serializers import (
    CreateReportSerializer,
    ReportSerializer,
)
from server.apps.hincal.models import Report
from server.apps.hincal.services.create_report import ReportWithContext
from server.apps.hincal.services.offers_and_wishes_for_report import (
    add_offers_and_wishes_in_context,
)
from server.apps.hincal.services.report_file import ReportFile
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListDeleteViewSet


class ReportFilter(
    UserFilterMixin,
    CreatedUpdatedDateFilterMixin,
    django_filters.FilterSet,
):
    """Фильтр отчетов."""

    class Meta(object):
        model = Report
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
        )


class ReportViewSet(RetrieveListDeleteViewSet):
    """Отчет."""

    serializer_class = ReportSerializer
    create_serializer_class = CreateReportSerializer
    queryset = Report.objects.select_related('user')
    search_fields = (
        'user_email',
        'user_username',
        'user_first_name',
        'user_last_name',
        'user_middle_name',
    )
    ordering_fields = '__all__'
    filterset_class = ReportFilter
    permission_type_map = {
        **RetrieveListDeleteViewSet.permission_type_map,
        'calculator': None,
        'get_file': None,
    }

    def get_queryset(self):
        """Выдача экономических показателей.

        Суперпользователь видит все показатели.
        Остальные видят показатели в рамках своего бизнеса.
        """
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        if user.is_anonymous:
            return queryset.none()

        return queryset.filter(
            report__in=user.reports.all()
        )

    def retrieve(self, request, *args, **kwargs):
        """Обогащаем context необходимымы данными."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        add_offers_and_wishes_in_context(report=instance)
        return Response(serializer.data)

    @action(
        ['POST'],
        url_path='calculator',
        detail=False,
        serializer_class=CreateReportSerializer,
    )
    def calculator(self, request):
        """Расчет расходов.

        Калькулятор для расчета расходов.

        Доступно: любому пользователю.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        report = ReportWithContext(
            user=request.user,
            data=serializer.validated_data,
        ).formation_report()

        return Response(
            data=ReportSerializer(report).data,
            status=status.HTTP_201_CREATED,
        )

    @action(
        ['POST'],
        url_path='get-file',
        detail=True,
    )
    def get_file(self, request, pk: int):
        """Получить файл отчета.

        Файл отчета.

        Доступно: любому пользователю.
        """
        instance = self.get_object()
        if request.user.is_authenticated:
            add_offers_and_wishes_in_context(report=instance)

            report_file = ReportFile(
                document_format='docx',
                report=instance,
            )

            return FileResponse(
                report_file.generate(),
                content_type='application/pdf',
                filename=report_file.get_file_name(),
                status=status.HTTP_200_OK,
            )
        return Response(status=status.HTTP_403_FORBIDDEN)
