from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from server.apps.personal_cabinet.api.serializers import (
    BaseSectorSerializer,
    BaseSubSectorSerializer,
    BaseTerritorialLocationSerializer,
)
from server.apps.personal_cabinet.models import Business
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.services.validators import inn_validator


class BusinessSerializer(ModelSerializerWithPermission):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    territorial_location = BaseTerritorialLocationSerializer(
        label=_('Территориальное расположение'),
    )
    sector = BaseSectorSerializer(
        label=_('Отрасль'),
    )
    sub_sector = BaseSubSectorSerializer(
        label=_('Подотрасль'),
    )
    business_type_label = serializers.SerializerMethodField()
    tax_system_type_label = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = (
            'id',
            'user',
            'position',
            'business_type',
            'inn',
            'sector',
            'sub_sector',
            'territorial_location',
            'hid',
            'short_business_name',
            'full_business_name',
            'management_name',
            'management_position',
            'full_opf',
            'short_opf',
            'okved_code',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'country',
            'region',
            'city_area',
            'city_district',
            'phone',
            'email',
            'site',
            'tax_system_type',
            'tax_system_type_label',
            'permission_rules',
            'created_at',
            'updated_at',
            'business_type_label',
        )

    def get_business_type_label(
        self,
        business: Business,
    ):
        """Подпись к business_type."""
        return business.get_business_type_display()

    def get_tax_system_type_label(
        self,
        business: Business,
    ):
        """Подпись к tax_system_type."""
        return business.get_tax_system_type_display()


class CreateBusinessSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для добавления бизнеса.
    """

    class Meta:
        model = Business
        fields = (
            'position',
            'business_type',
            'inn',
            'sector',
            'sub_sector',
            'territorial_location',
            'hid',
            'short_business_name',
            'full_business_name',
            'management_name',
            'management_position',
            'full_opf',
            'short_opf',
            'okved_code',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'country',
            'region',
            'city_area',
            'city_district',
            'phone',
            'email',
            'site',
            'economic_activities',
        )

    def validate_inn(self, inn: str):
        """Валидация ИНН."""
        inn_validator(inn)
        return inn


class UpdateBusinessSerializer(ModelSerializerWithPermission):
    """Изменение бизнеса."""

    class Meta:
        model = Business
        fields = (
            'sector',
            'sub_sector',
            'territorial_location',
            'short_business_name',
            'full_business_name',
            'management_name',
            'management_position',
            'full_opf',
            'short_opf',
            'okved_code',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'country',
            'region',
            'city_area',
            'city_district',
            'phone',
            'email',
            'site',
            'economic_activities',
        )


class CreateBusinessByInnSerializer(ModelSerializerWithPermission):
    """Сериалайзер создания бизнеса по ИНН."""

    class Meta:
        model = Business
        fields = (
            'inn',
        )

    def validate_inn(self, inn: str):
        """Валидация ИНН."""
        inn_validator(inn)
        return inn
