from server.apps.hincal.models import Archive
from server.apps.services.serializers import ModelSerializerWithPermission


class ArchiveSerializer(ModelSerializerWithPermission):
    """Сериалайзер архива."""

    class Meta(object):
        model = Archive
        fields = (
            'id',
            'year',
            'income_tax_rate_to_the_subject_budget',
            'income_tax_rate_to_the_federal_budget',
            'land_tax_rate',
            'property_tax_rate',
            'patent_tax_rate',
            'osn_tax_rate',
            'ysn_tax_rate',
            'personal_income_rate',
            'pension_contributions_rate',
            'medical_contributions_rate',
            'disability_contributions_rate',
            'lower_margin_error',
            'upper_margin_error',
            'cost_accounting',
            'registration_costs',
            'avg_land_cadastral_value',
            'avg_land_lease_costs',
            'avg_land_purchase_costs',
            'avg_property_cadastral_value',
            'avg_property_lease_costs',
            'avg_property_purchase_costs',
            'is_actual',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class ArchiveForReportSerializer(ModelSerializerWithPermission):
    """Сериалайзер архива для контекста."""

    class Meta(object):
        model = Archive
        fields = (
            'year',
            'income_tax_rate_to_the_subject_budget',
            'income_tax_rate_to_the_federal_budget',
            'land_tax_rate',
            'property_tax_rate',
            'patent_tax_rate',
            'osn_tax_rate',
            'ysn_tax_rate',
            'personal_income_rate',
            'pension_contributions_rate',
            'medical_contributions_rate',
            'disability_contributions_rate',
            'lower_margin_error',
            'upper_margin_error',
            'cost_accounting',
            'registration_costs',
            'avg_land_cadastral_value',
            'avg_land_lease_costs',
            'avg_land_purchase_costs',
            'avg_property_cadastral_value',
            'avg_property_lease_costs',
            'avg_property_purchase_costs',
        )
