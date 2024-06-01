import re
from typing import Optional, Tuple

from allauth.account.forms import default_token_generator
from django.utils.translation import gettext as _
from rest_framework.exceptions import NotFound

from server.apps.services.exception import ApiError
from server.apps.user.models import User

CONFIRM_EMAIL_REGEXP = re.compile('(?P<email>.+)/(?P<key>.+)')


def check_extra_path(
    extra_path: str,
) -> Optional[Tuple[str, ...]]:
    """Проверка корректности extra_path, при подтверждении почты."""
    match = CONFIRM_EMAIL_REGEXP.match(extra_path)
    if match:
        return match.groups()

    raise ApiError(
        _(
            'Не удалось извлечь email пользователя и ключ для ' +
            'подтверждения email',
        ),
    )


def get_user_by_email_and_check_token(email: str, key: str):
    """Получаем пользователя по e-mail и проверяем токен."""
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise NotFound(_('Пользователь не найден'))

    if not default_token_generator.check_token(user, key):
        raise ApiError(_('Токен подтверждения регистрации не действителен'))

    return user
