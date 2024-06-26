from server.apps.investment_object.api.serializers import (
    BaseEconomicActivitySerializer,
    BaseRestrictionSerializer,
)
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.models import ServiceSupport


class ListServiceSupportSerializer(ModelSerializerWithPermission):
    """Сериалайзер сервиса поддержки."""

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
            'external_id',
            'region',
            'service_support_type',
            'name',
            'support_type',
            'support_level',
            'description',
            'legal_act',
            'url_legal_act',
            'url_application_form',
            'name_responsible_body',
            'msp_roster',
            'applicant_requirement',
            'applicant_procedure',
            'required_document',
            'url',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class DetailServiceSupportSerializer(ModelSerializerWithPermission):
    """Сериалайзер сервиса поддержки."""

    economic_activities = BaseEconomicActivitySerializer(many=True)
    restrictions = BaseRestrictionSerializer(many=True)

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
            'external_id',
            'region',
            'service_support_type',
            'name',
            'support_type',
            'support_level',
            'description',
            'legal_act',
            'url_legal_act',
            'url_application_form',
            'name_responsible_body',
            'economic_activities',
            'restrictions',
            'msp_roster',
            'applicant_requirement',
            'applicant_procedure',
            'required_document',
            'content_type_id',
            'permission_rules',
            'url',
            'content_type_id',
            'created_at',
            'updated_at',
        )
