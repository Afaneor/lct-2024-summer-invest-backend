import django_filters
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.personal_cabinet.api.serializers import (
    BusinessSerializer,
    CreateBusinessByInnSerializer,
    CreateBusinessSerializer,
    UpdateBusinessSerializer,
)
from server.apps.personal_cabinet.models import Business
from server.apps.personal_cabinet.services.create_business import (
    update_or_create_business,
)
from server.apps.services.filters_mixins import (
    CreatedUpdatedDateFilterMixin,
    UserFilterMixin,
)
from server.apps.services.views import RetrieveListCreateUpdateDeleteViewSet


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

    class Meta:
        model = Business
        fields = (
            'id',
            'user',
            'user_email',
            'user_username',
            'user_first_name',
            'user_last_name',
            'user_middle_name',
            'business_type',
            'inn',
            'sector',
            'sub_sector',
            'territorial_location',
            'short_business_name',
            'address',
            'email',
            'site',
        )


class BusinessViewSet(RetrieveListCreateUpdateDeleteViewSet):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    create_serializer_class = CreateBusinessSerializer
    update_serializer_class = UpdateBusinessSerializer
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
    permission_type_map = {
        **RetrieveListCreateUpdateDeleteViewSet.permission_type_map,
        'create_business_by_inn': 'add',
        'update_business_by_inn': 'change',
    }

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

    def perform_create(self, serializer):
        """
        Добавляем информацию о пользователе.
        """
        serializer.validated_data.update(user=self.request.user)
        serializer.save()

    @action(
        methods=['POST'],
        url_path='create-business-by-inn',
        detail=False,
        serializer_class=CreateBusinessByInnSerializer,
    )
    def create_business_by_inn(
        self,
        request: Request,
    ):
        """Создание бизнеса по ИНН."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # noqa: WPS204
        try:
            business, created = update_or_create_business(
                inn=serializer.validated_data['inn'],
                user_id=request.user.id,
            )
        except Exception:
            return Response(
                data={
                    'detail': _(
                        'При добавлении по ИНН вашего бизнеса произошла '
                        'ошибка, связанная с доступом к сервису DaData.'
                        'Вы можете добавить информацию в ручную.'
                    ),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if business:
            detail = _('Информация о бизнесе найдена и добавлена')
        else:
            detail = _(
                'Информация о бизнесе не найдена. '
                'Проверьте указанный ИНН.'
                'Также можете добавить организацию в ручную.'

            )

        return Response(
            data={'detail': detail},
            status=status.HTTP_200_OK,
        )

    @action(
        methods=['PUT', 'PATCH'],
        url_path='update-business-by-inn',
        detail=False,
    )
    def update_business_by_inn(
        self,
        request: Request,
    ):
        """Обновление бизнеса по ИНН."""
        business = self.get_object()
        try:
            business, created = update_or_create_business(
                inn=business.inn,
                user_id=request.user.id,
            )
        except Exception:
            return Response(
                data={
                    'detail': _(
                        'При обновлении по ИНН вашего бизнеса произошла '
                        'ошибка, связанная с доступом к сервису DaData.'
                        'Вы можете обновить информацию в ручную.'
                    ),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if business:
            detail = _('Информация о бизнесе успешно обновлена')
        else:
            detail = _(
                'Информация о бизнесе  не найдена. '
                'Информация не обновлена',
            )

        return Response(
            data={'detail': detail},
            status=status.HTTP_200_OK,
        )
