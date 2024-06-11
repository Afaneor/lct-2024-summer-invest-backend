from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from server.apps.services.validators import inn_validator
from server.apps.user.models import User


class RegisterSerializer(serializers.Serializer):
    """Регистрация пользователя."""

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    middle_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    email = serializers.EmailField(required=True)
    inn = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def validate_inn(self, inn: str):
        """Валидация ИНН."""
        inn_validator(inn)
        return inn

    def is_valid(self, raise_exception=False) -> bool:
        """Проверка валидности данных для регистрации пользователя."""
        self._validate_email()
        self._validate_password()

        return super().is_valid(raise_exception=True)

    def _validate_email(self) -> None:
        """Валидация email."""
        if User.objects.filter(email=self.initial_data['email']).exists():
            initial_email = self.initial_data['email']
            raise ValidationError(
                {
                    'email': [_(
                        f'Пользователь с email {initial_email} ' +
                        'уже существует, укажите другой email или ' +
                        'попробуйте восстановить пароль.',
                    )],
                },
            )

    def _validate_password(self):  # noqa: WPS238
        """Валидация паролей."""
        password1 = self.initial_data.get('password1', None)
        password2 = self.initial_data.get('password2', None)

        if not password1:
            raise ValidationError(
                {'password1': [_('Необходимо указать пароль')]},
            )

        if not password2:
            raise ValidationError(
                {'password2': [_('Необходимо указать пароль два раза')]},
            )

        if password1 != password2:
            raise ValidationError(
                {'password': [_('Оба пароля должны совпадать')]},
            )

        try:
            validate_password(str(password1))
        except DjangoValidationError as exc:
            raise ValidationError(exc.messages)
