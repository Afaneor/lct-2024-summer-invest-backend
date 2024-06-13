from rest_framework import serializers

from server.apps.personal_cabinet.models import Subscription
from server.apps.services.serializers import ModelSerializerWithPermission


class SubscriptionSerializer(ModelSerializerWithPermission):
    """Сериалайзер подписки."""

    subscription_type_label = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = (
            'id',
            'user',
            'subscription_type',
            'subscription_type_label',
            'email',
            'telegram_username',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_subscription_type_label(
        self,
        subscription: Subscription,
    ):
        """Подпись к subscription_type."""
        return subscription.get_subscription_type_display()


class CreateSubscriptionSerializer(serializers.ModelSerializer):
    """Сериалайзер создания подписки."""

    class Meta:
        model = Subscription
        fields = (
            'subscription_type',
            'email',
            'telegram_username',
            'topics',
            )


class UpdateSubscriptionSerializer(serializers.ModelSerializer):
    """Сериалайзер изменения подписки."""

    class Meta:
        model = Subscription
        fields = (
            'email',
            'telegram_username',
            'topics',
        )
