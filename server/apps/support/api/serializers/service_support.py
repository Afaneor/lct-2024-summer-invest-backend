from rest_framework import serializers

from server.apps.investment_object.api.serializers import (
    BaseEconomicActivitySerializer,
    BaseRestrictionSerializer,
)
from server.apps.service_interaction.api.serializers.base_data import \
    BaseFeedbackSerializer
from server.apps.service_interaction.models import Feedback
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.models import ServiceSupport


class ListServiceSupportSerializer(ModelSerializerWithPermission):
    """Сериалайзер сервиса поддержки."""

    economic_activities = BaseEconomicActivitySerializer(many=True)
    restrictions = BaseRestrictionSerializer(many=True)
    feedbacks = serializers.SerializerMethodField()

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
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
            'feedbacks',
            'content_type_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_feedbacks(self, service_support: ServiceSupport):
        """Отзывы на объект."""
        return BaseFeedbackSerializer(
            Feedback.objects.filter(
                object_id=service_support.id,
                content_type_id=service_support.content_type_id,
            ),
            many=True,
        ).data


class DetailServiceSupportSerializer(ModelSerializerWithPermission):
    """Сериалайзер сервиса поддержки."""

    economic_activities = BaseEconomicActivitySerializer(many=True)
    restrictions = BaseRestrictionSerializer(many=True)
    feedbacks = serializers.SerializerMethodField()

    class Meta:
        model = ServiceSupport
        fields = (
            'id',
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
            'content_type_id',
            'feedbacks',
            'created_at',
            'updated_at',
        )

    def get_feedbacks(self, service_support: ServiceSupport):
        """Отзывы на объект."""
        return BaseFeedbackSerializer(
            Feedback.objects.filter(
                object_id=service_support.id,
                content_type_id=service_support.content_type_id,
            ),
            many=True,
        ).data
