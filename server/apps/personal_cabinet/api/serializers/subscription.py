from rest_framework import serializers

from server.apps.personal_cabinet.models import Subscription
from server.apps.services.serializers import ModelSerializerWithPermission


class SubscriptionSerializer(ModelSerializerWithPermission):
    """Сериалайзер подписки."""

    class Meta:
        model = Subscription
        fields = (
            'id',
            'user',
            'subscription_type',
            'telegram_username',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class CreateSubscriptionSerializer(serializers.ModelSerializer):
    """Сериалайзер создания подписки."""

    class Meta:
        model = Subscription
        fields = (
            'subscription_type',
            'telegram_username',
            'topics',
            'events',
        )


class UpdateSubscriptionSerializer(serializers.ModelSerializer):
    """Сериалайзер изменения подписки."""

    class Meta:
        model = Subscription
        fields = (
            'telegram_username',
            'topics',
            'events',
        )
