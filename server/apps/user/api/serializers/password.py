from typing import Optional

from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from server.apps.user.models import User
from server.apps.user.services.reset_password import check_new_password


class ResetPasswordRequestSerializer(serializers.Serializer):
    """Восстановление забытого пользователем пароля. Этап №1."""

    email = serializers.EmailField(required=True)

    user: Optional[User] = None

    def is_valid(self, raise_exception=False) -> bool:
        """Валидность email для восстановления пароля."""
        email = self.initial_data.get('email', None)
        self.check_email(email)
        return super().is_valid(raise_exception=raise_exception)

    def check_email(self, email) -> None:
        """Проверяем, что пользователь с такой почтой существует."""
        try:
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError(
                {'email': [_('Пользователя с таким email не существует')]},
            )


class ResetPasswordConfirmSerializer(serializers.Serializer):
    """Успешное восстановление пароля пользователя. Этап №2."""

    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def is_valid(self, raise_exception=False)  -> bool:
        """Валидация корректности пароля."""
        password1 = self.initial_data.get('password1')
        password2 = self.initial_data.get('password2')
        check_new_password(password1=password1, password2=password2)

        return super().is_valid(raise_exception=raise_exception)


class ChangePasswordSerializer(serializers.Serializer):
    """Изменение пароля."""

    password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate_password(self, password: str) -> str:
        """Проверка корректности введенного пароля."""
        user = self.context.get('request').user
        if check_password(password, user.password):
            return password
        raise ValidationError(
            {'password': [_('Вы ввели некорректный пароль')]},
        )

    def is_valid(self, raise_exception=False)  -> bool:
        """Валидация корректности пароля."""
        password1 = self.initial_data.get('password1')
        password2 = self.initial_data.get('password2')
        check_new_password(password1=password1, password2=password2)

        return super().is_valid(raise_exception=raise_exception)

    def update(self, instance: User, validated_data):
        """Изменение пароля."""
        instance.set_password(validated_data.get('new_password1'))
        instance.save(update_fields=['password'])
        return instance
