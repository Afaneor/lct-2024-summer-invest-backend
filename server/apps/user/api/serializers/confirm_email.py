from typing import Optional

from rest_framework import serializers

from server.apps.user.models import User
from server.apps.user.services.check_user import check_user_active


class ConfirmEmailRequestSerializer(serializers.Serializer):
    """Сериализатор отправки сообщения подтверждения регистрации."""

    email = serializers.EmailField(required=True)

    user: Optional[User] = None

    def is_valid(self, raise_exception=False)  -> bool:
        """Валидность email для восстановления пароля."""
        email = self.initial_data.get('email', None)
        self.check_email(email)
        return True

    def check_email(self, email) -> None:
        self.user = check_user_active(email=email)
        return self.user


class ConfirmEmailProcessSerializer(serializers.Serializer):
    """Успешное подтверждение регистрации.

    Сериализитор не несет смысловой нагрузки, но нужен для того, чтобы
    не удалось случайно активировать аккаунт у пользователя.
    """

    is_active = serializers.BooleanField(required=True)
