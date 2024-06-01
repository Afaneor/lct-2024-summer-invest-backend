import re

from allauth.account.forms import default_token_generator
from allauth.account.utils import url_str_to_user_pk
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError

from server.apps.services.exception import ApiError
from server.apps.user.models import User

# Регулярное выражение для проверки на корректность пути сброса пароля
RESET_PASSWORD_REGEXP = re.compile('(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)')


def get_user_reset_password_process(extra_path: str) -> AbstractUser:
    """Проверка валидности токена сброса пароля."""
    # Выделяем необходимые нам параметры для сброса пароля
    match = RESET_PASSWORD_REGEXP.match(extra_path)
    if match:
        uidb36, key = match.groups()

        return get_user_by_token(uidb36, key)

    raise ApiError(
        _('Не удалось извлечь id пользователя и ключ сброса пароля'),
    )


def get_user_by_token(uidb36_inner: str, key: str) -> AbstractUser:
    """Получение пользователя по ключу и id пользователя."""
    pk = url_str_to_user_pk(uidb36_inner)

    try:
        reset_user = User.objects.get(pk=pk)
    except (ValueError, User.DoesNotExist):
        raise ApiError(_('Пользователь не найден'))

    invalid_token = not default_token_generator.check_token(
        reset_user,
        key,
    )
    if reset_user is None or invalid_token:
        raise ApiError(_('Токен сброса пароля не действителен'))
    return reset_user


def set_new_password(extra_path: str, password: str):
    """Установка нового пароля для пользователя."""
    user = get_user_reset_password_process(extra_path=extra_path)
    user.set_password(password)

    # Активация аккаунта пользователя и создание профиля.
    if not user.is_active:
        user.is_active = True

    user.save(update_fields=['password', 'is_active'])


def check_new_password(password1: str, password2: str) -> None:
    """Проверка совпадения и корректности нового пароля."""
    if password1 != password2:
        raise ValidationError(
            {
                'new_password': [
                    _(
                        'Пароли должны совпадать! ' +
                        'Проверьте корректность данных',
                    ),
                ],
            },
        )
    try:
        validate_password(str(password1))
    except DjangoValidationError as exc:
        raise ValidationError(exc.messages)
