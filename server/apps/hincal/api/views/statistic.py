from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rules.contrib.rest_framework import AutoPermissionViewSetMixin

from server.apps.hincal.api.serializers import (
    AllStatisticSerializer,
    UserStatisticSerializer,
)
from server.apps.hincal.services.statistic import (
    get_all_statistics,
    get_user_statistics,
)


class StatisticViewSet(
    AutoPermissionViewSetMixin,
    NestedViewSetMixin,
    GenericViewSet,
):
    """Общая статистика по системе и для пользователя."""

    permission_type_map = {
        **AutoPermissionViewSetMixin.permission_type_map,
        'all': None,
        'user': None,
        'metadata': None,
    }

    @action(
        ['GET'],
        url_path='all',
        detail=False,
        serializer_class=AllStatisticSerializer,
    )
    def all(self, request):
        """Получить общую статистику по системе."""
        serializer = self.get_serializer(data=get_all_statistics())
        serializer.is_valid(raise_exception=True)  # noqa: WPS204

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    @action(
        ['GET'],
        url_path='user',
        detail=False,
        serializer_class=UserStatisticSerializer,
    )
    def user(self, request):
        """Получить статистику по пользователю."""
        if request.user.is_authenticated:
            serializer = self.get_serializer(
                data=get_user_statistics(user=request.user),
            )
            serializer.is_valid(raise_exception=True)  # noqa: WPS204

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(status=status.HTTP_403_FORBIDDEN)
