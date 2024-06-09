from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin

from server.apps.services.enums import BusinessType


class DefaultUserManager(UserManager):  # type: ignore
    """Менеджер для пользователей с логином email."""

    use_in_migrations = True

    def create_user(
        self,
        username=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Создание пользователя."""
        if username is None:
            username = email
        return super().create_user(
            username,
            email,
            password,
            **extra_fields,
        )

    def create_superuser(
        self,
        username=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Создание суперпользователя."""
        if username is None:
            username = email
        return super().create_superuser(
            username,
            email,
            password,
            **extra_fields,
        )


class User(  # type: ignore
    RulesModelMixin,
    AbstractUser,
    metaclass=RulesModelBase,
):
    """Кастомный класс пользователя."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    avatar = models.ImageField(
        verbose_name=_('Аватар'),
        upload_to='media',
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_('Адрес электронной почты'),
        unique=True,
    )
    middle_name = models.CharField(
        verbose_name=_('Отчество'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    objects = DefaultUserManager()  # noqa: WPS110

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.email

    @property
    def full_name(self) -> str:
        """ФИО пользователя."""
        names_elements = (self.last_name, self.first_name, self.middle_name)
        if not any(names_elements):
            return ''
        return ' '.join(filter(None, names_elements)).strip()

    @property
    def is_need_add_info(self) -> bool:
        """
        Необходимость заполнения информации о бизнесе.

        Если у пользователя нет информации о бизнесе, то заставляем его
        заполнить такую информацию.
        Если пользователь физическое лицо, то заставляем заполнить информацию.
        """
        for business in self.businesses.all():
            if (
                business.BusinessType != BusinessType.PHYSICAL or
                business.sector is not None or
                business.sub_sector is not None
            ):
                return False

        return True
