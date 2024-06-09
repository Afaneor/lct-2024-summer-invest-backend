from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from server.apps.investment_object.api.serializers.base_data import (
    BaseReadyBusinessSerializer,
    BaseRealEstateSerializer,
    BaseSpecializedSiteSerializer,
    BaseTenderLotSerializer,
)
from server.apps.investment_object.models import InvestmentObject
from server.apps.service_interaction.api.serializers.base_data import (
    BaseFeedbackSerializer,
)
from server.apps.service_interaction.models import Feedback
from server.apps.services.enums import UploadDataFromFileType
from server.apps.services.serializers import ModelSerializerWithPermission


class ListInvestmentObjectSerializer(ModelSerializerWithPermission):
    """Сериалайзер инвестиционных площадок."""

    tender_lot = BaseTenderLotSerializer()
    real_estate = BaseRealEstateSerializer()
    specialized_site = BaseSpecializedSiteSerializer()
    ready_business = BaseReadyBusinessSerializer()
    feedbacks = serializers.SerializerMethodField()

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'external_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'object_type',
            'url',
            'extra_data',
            'longitude',
            'latitude',
            'tender_lot',
            'real_estate',
            'specialized_site',
            'ready_business',
            'feedbacks',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_feedbacks(self, investment_object: InvestmentObject):
        """Отзывы на объект."""
        return BaseFeedbackSerializer(
            Feedback.objects.filter(
                object_id=investment_object.id,
                conent_type_id=investment_object.content_type_id,
            )
        ).data


class DetailInvestmentObjectSerializer(ModelSerializerWithPermission):
    """Сериалайзер инвестиционных площадок."""

    tender_lot = BaseTenderLotSerializer()
    real_estate = BaseRealEstateSerializer()
    specialized_site = BaseSpecializedSiteSerializer()
    ready_business = BaseReadyBusinessSerializer()
    feedbacks = serializers.SerializerMethodField()

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'external_id',
            'main_photo_url',
            'photo_urls',
            'name',
            'object_type',
            'url',
            'extra_data',
            'longitude',
            'latitude',
            'tender_lot',
            'real_estate',
            'specialized_site',
            'ready_business',
            'content_type_id',
            'feedbacks',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_feedbacks(self, investment_object: InvestmentObject):
        """Отзывы на объект."""
        return BaseFeedbackSerializer(
            Feedback.objects.filter(
                object_id=investment_object.id,
                conent_type_id=investment_object.content_type_id,
            )
        ).data


class UploadDataFromFileSerializer(serializers.Serializer):
    """Загрузка xlsx-файла с информацией об объектах."""

    file = serializers.FileField(required=True)
    object_type = serializers.ChoiceField(
        required=True,
        choices=UploadDataFromFileType.choices,
    )

    def validate_file(self, file: InMemoryUploadedFile) -> InMemoryUploadedFile:
        """Проверка файла."""
        if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            raise ValidationError(
                _('Возможно загружать только xlsx-файл.'),
            )
        return file
