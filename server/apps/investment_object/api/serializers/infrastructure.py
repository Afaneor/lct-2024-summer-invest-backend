from server.apps.investment_object.models import Infrastructure
from server.apps.services.serializers import ModelSerializerWithPermission


class InfrastructureSerializer(ModelSerializerWithPermission):
    """Сериалайзер инфраструктуры."""

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
            'permission_rules',
            'created_at',
            'updated_at',
        )
