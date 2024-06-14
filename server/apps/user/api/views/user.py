import django_filters
from allauth.account.forms import default_token_generator
from django.conf import settings
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response

from server.apps.services.views import RetrieveListUpdateViewSet
from server.apps.user.api.serializers import (
    ChangePasswordSerializer,
    ConfirmEmailRequestSerializer,
    LoginSerializer,
    RegisterSerializer,
    ResetPasswordConfirmSerializer,
    ResetPasswordRequestSerializer,
    UserSerializer,
)
from server.apps.user.models import User
from server.apps.user.services.confirm_email import (
    check_extra_path,
    get_user_by_email_and_check_token,
)
from server.apps.user.services.create_user import create_new_user
from server.apps.user.services.reset_password import (
    get_user_reset_password_process,
    set_new_password,
)
from server.apps.user.services.send_email import (
    send_confirm_email,
    send_email_with_reset_password,
)


class UserFilter(django_filters.FilterSet):
    """Фильтр для модели пользователя."""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'is_active',
        )


class UserViewSet(RetrieveListUpdateViewSet):
    """Пользователь. Просмотр/создание/изменение.

    Описание: Админы платформы могут добавить пользователя в систему, а сами
    пользователи могут только просматривать информацию.
    Изменение информации о пользователе (ФИО) доступно через профиль.
    Добавление/регистрация пользователя происходит через POST запрос.

    Доступно: суперпользователю и владельцу уведомлений.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    filterset_class = UserFilter
    ordering_fields = '__all__'
    permission_type_map = {
        **RetrieveListUpdateViewSet.permission_type_map,
        'login': None,
        'register': None,
        'confirm_email_request': None,
        'confirm_email_process': None,
        'reset_password_request': None,
        'reset_password_process': None,
        'change_password': 'action_is_authenticated',
        'get_info': 'action_is_authenticated',
        'logout': 'action_is_authenticated',
    }

    def get_queryset(self):
        """Выдача информации о пользователях."""
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        if user.is_anonymous:
            return queryset.none()

        return queryset.filter(id=user.id)

    @action(
        ['POST'],
        url_path='login',
        detail=False,
        serializer_class=LoginSerializer,
    )
    def login(self, request):
        """Авторизация пользователя.

        Общее описание: пользователь с указанными данными авторизуется с
        помощью сессии.

        Доступно: любому пользователю.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # noqa: WPS204
        try:
            login(
                request,
                serializer.user,
            )
        except Exception:
            raise NotFound(
                _('Пользователь с указанными данными не найден'),
            )

        return Response(
            data={'is_need_add_info': serializer.user.is_need_add_info},
            status=status.HTTP_200_OK
        )

    @action(
        ['POST'],
        detail=False,
        url_path='register',
        serializer_class=RegisterSerializer,
    )
    def register(self, request):  # noqa: WPS210
        """Регистрация пользователя.

        Процесс регистрации пользователя.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_new_user(data=serializer.validated_data)

        # Отправляем письмо активации пользователя
        send_confirm_email(
            request=request,
            user=user,
        )

        return Response(
            data=UserSerializer(user).data,
            status=status.HTTP_201_CREATED,
        )

    @action(
        methods=['POST'],
        detail=False,
        url_path='resend-email-confirmation',
        serializer_class=ConfirmEmailRequestSerializer,
    )
    def confirm_email_request(self, request):
        """Повторная отправка сообщения об активации аккаунта.

        Общее описание: api позволяет направить письмо для активации аккаунта
        пользователя.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Отправляем письмо активации пользователя
        send_confirm_email(
            user=serializer.user,
            request=request,
        )

        return Response(
            data={
                'detail': _(
                    'На указанный адрес электронной почты ' +
                    'отправлено письмо с подтверждением ' +
                    'регистрации',
                ),
            },
            status=status.HTTP_200_OK,
        )

    @action(
        methods=['GET', 'POST'],
        detail=False,
        url_path='confirm-email/(?P<extra_path>.+)?',
    )
    def confirm_email_process(self, request, extra_path=None):
        """Подтверждение регистрации.

        Процесс подтверждения регистрации.
        """
        if request.method == 'GET':
            # Проверка токена.
            email, key = check_extra_path(extra_path)
            user = get_user_by_email_and_check_token(email, key)
            return Response(
                data=UserSerializer(user).data,
                status=status.HTTP_200_OK,
            )

        # Проверка токена.
        email, key = check_extra_path(extra_path)
        user = get_user_by_email_and_check_token(email, key)

        if not default_token_generator.check_token(user, key):
            raise ParseError(
                _('Некорректный ключ подтверждения активации'),
            )

        if user.is_active:
            return HttpResponseRedirect(settings.EMAIL_CONFIRM_REDIRECT_URL)

        user.is_active = True
        user.save()

        return HttpResponseRedirect(settings.EMAIL_CONFIRM_REDIRECT_URL)

    @action(
        methods=['POST'],
        url_path='send-reset-password-email',
        detail=False,
        serializer_class=ResetPasswordRequestSerializer,
    )
    def reset_password_request(self, request):
        """Запрос сброса пароля.

        Общее описание: api позволяет запросить письмо с инструкцией по
        сбросу пароля.

        Доступно: любому пользователю.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_email_with_reset_password(
            user=serializer.user,
            request=request,
        )

        return Response(
            data={
                'detail':
                    _(
                        'На указанный адрес электронной почты отправлено ' +
                        'письмо с инструкцией по восстановлению пароля',
                    ),
            },
            status=status.HTTP_200_OK,
        )

    @action(  # type: ignore
        methods=['GET', 'POST'],
        detail=False,
        url_path='reset-password/(?P<extra_path>.+)?',
        serializer_class=ResetPasswordConfirmSerializer,
    )
    def reset_password_process(self, request, extra_path: str):
        """Сброс пароля пользователя.

        Общее описание: api позволяет установить новый пароль пользователю.

        Доступно: любому пользователю.
        """
        if request.method == 'GET':
            user = get_user_reset_password_process(extra_path)
            return Response(
                data=UserSerializer(user).data,  # type: ignore
                status=status.HTTP_200_OK,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        set_new_password(
            extra_path=extra_path,
            password=serializer.validated_data.get('password1'),
        )

        return Response(
            data={'detail': _('Новый пароль успешно установлен')},
            status=status.HTTP_200_OK,
        )

    @action(
        ['PATCH', 'PUT'],
        detail=False,
        url_path='change-password',
        serializer_class=ChangePasswordSerializer,
    )
    def change_password(self, request):
        """Смена пароля.

        Общее описание: api позволяет изменить старый пароль на новый.

        Доступно: любому только авторизованному пользователю.
        """
        serializer = self.get_serializer(
            instance=request.user,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={'detail': _('Пароль успешно изменен')},
            status=status.HTTP_200_OK,
        )

    @action(
        methods=['GET'],
        detail=False,
        url_path='get-info',
        serializer_class=UserSerializer,
    )
    def get_info(self, request):
        """Получение информации о пользователе.

        Детальная информация о пользователе.
        """
        serializer = self.get_serializer(request.user)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    @action(
        ['POST'],
        detail=False,
        url_path='logout',
    )
    def logout(self, request):
        """Выход из системы.

        Общее описание: api позволяет пользователю выйти из системы.

        Доступно: любому только авторизованному пользователю.
        """
        logout(request)

        return Response(
            data={'detail': _('Пользователь успешно вышел из системы')},
            status=status.HTTP_200_OK,
        )
