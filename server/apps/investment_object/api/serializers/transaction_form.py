from rest_framework import serializers

from server.apps.investment_object.models import TransactionForm
from server.apps.services.serializers import ModelSerializerWithPermission


class TransactionFormSerializer(ModelSerializerWithPermission):
    """Сериалайзер формы сделки."""

    transaction_form_type_label = serializers.SerializerMethodField()

    class Meta:
        model = TransactionForm
        fields = (
            'id',
            'name',
            'transaction_form_type',
            'transaction_form_type_label',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_transaction_form_type_label(
        self,
        transaction_form: TransactionForm,
    ):
        """Подпись к transaction_form_type."""
        return transaction_form.get_transaction_form_type_display()
