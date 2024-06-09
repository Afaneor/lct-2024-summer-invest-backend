from server.apps.investment_object.models import TransactionForm
from server.apps.services.serializers import ModelSerializerWithPermission


class TransactionFormSerializer(ModelSerializerWithPermission):
    """Сериалайзер формы сделки."""

    class Meta:
        model = TransactionForm
        fields = (
            'id',
            'name',
            'transaction_form_type',
            'permission_rules',
            'created_at',
            'updated_at',
        )
