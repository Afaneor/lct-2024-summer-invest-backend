from rest_framework import serializers

from server.apps.investment_object.models import Infrastructure
from server.apps.services.serializers import ModelSerializerWithPermission


class InfrastructureSerializer(ModelSerializerWithPermission):
    """Сериалайзер инфраструктуры."""

    availability_label = serializers.SerializerMethodField()

    class Meta:
        model = Infrastructure
        fields = (
            'id',
            'name',
            'consumption_tariff',
            'transportation_tariff',
            'max_allowable_power',
            'free_power',
            'throughput',
            'other_characteristics',
            'availability',
            'availability_label',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_availability_label(
        self,
        infrastructure: Infrastructure,
    ):
        """Подпись к availability."""
        return infrastructure.get_availability_display()
