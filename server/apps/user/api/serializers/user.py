from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.apps.personal_cabinet.services.enums import TypeBusiness
from server.apps.services.serializers import ModelSerializerWithPermission

User = get_user_model()


class BaseInfoUserSerializer(serializers.ModelSerializer):
    """Сериалайзер пользователя. Используется в других сериалайзерах."""

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'middle_name',
        )


class UserSerializer(ModelSerializerWithPermission):
    """Детальная информация о пользователе."""

    class Meta:
        model = User
        fields = (
            'id',
            'avatar',
            'username',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'full_name',
            'is_active',
            'is_need_add_info',
            'permission_rules',
        )
