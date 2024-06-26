from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from server.apps.investment_object.api.serializers.base_data import (
    BaseEconomicActivitySerializer,
    BaseReadyBusinessSerializer,
    BaseRealEstateSerializer,
    BaseSpecializedSiteSerializer,
    BaseTenderLotSerializer,
    BaseTransactionFormSerializer,
)
from server.apps.investment_object.models import InvestmentObject
from server.apps.services.enums import UploadDataFromFileType
from server.apps.services.serializers import ModelSerializerWithPermission


class ListInvestmentObjectSerializer(ModelSerializerWithPermission):
    """Сериалайзер инвестиционных площадок."""

    tender_lot = BaseTenderLotSerializer()
    real_estate = BaseRealEstateSerializer()
    specialized_site = BaseSpecializedSiteSerializer()
    ready_business = BaseReadyBusinessSerializer()
    transaction_form = BaseTransactionFormSerializer()
    economic_activities = BaseEconomicActivitySerializer(many=True)

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'main_photo_url',
            'photo_urls',
            'object_type',
            'economic_activities',
            'transaction_form',
            'cost',
            'land_area',
            'building_area',
            'url',
            'location',
            'data_source',
            'longitude',
            'latitude',
            'tender_lot',
            'real_estate',
            'specialized_site',
            'ready_business',
            'permission_rules',
            'created_at',
            'updated_at',
        )


class DetailInvestmentObjectSerializer(ModelSerializerWithPermission):
    """Сериалайзер инвестиционных площадок."""

    tender_lot = BaseTenderLotSerializer()
    real_estate = BaseRealEstateSerializer()
    specialized_site = BaseSpecializedSiteSerializer()
    ready_business = BaseReadyBusinessSerializer()
    transaction_form = BaseTransactionFormSerializer()
    economic_activities = BaseEconomicActivitySerializer(many=True)

    class Meta:
        model = InvestmentObject
        fields = (
            'id',
            'name',
            'main_photo_url',
            'photo_urls',
            'object_type',
            'economic_activities',
            'transaction_form',
            'cost',
            'land_area',
            'building_area',
            'url',
            'location',
            'data_source',
            'longitude',
            'latitude',
            'tender_lot',
            'real_estate',
            'specialized_site',
            'ready_business',
            'content_type_id',
            'permission_rules',
            'created_at',
            'updated_at',
        )


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
