from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from server.apps.user.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """Класс админки пользователя."""

    list_display = (
        'id',
        'email',
        'username',
        'last_name',
        'first_name',
        'is_superuser',
    )
    search_fields = (
        'last_name',
        'first_name',
        'username',
        'email',
    )
    list_filter = ('is_superuser', 'is_active')
    ordering = (
        'id',
        'email',
        'username',
        'last_name',
        'first_name',
        'is_superuser',
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'email'),
            },
        ),
    )
