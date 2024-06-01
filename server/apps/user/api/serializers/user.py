from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.apps.services.serializers import ModelSerializerWithPermission

User = get_user_model()


class BaseInfoUserSerializer(serializers.ModelSerializer):
    """Сериалайзер пользователя. Используется в других сериалайзерах."""

    class Meta(object):
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

    class Meta(object):
        model = User
        fields = (
            'id',
            'avatar',
            'username',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'is_active',
            'permission_rules',
        )
