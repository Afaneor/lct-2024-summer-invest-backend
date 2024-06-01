from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from taggit.serializers import TagListSerializerField

from server.apps.hincal.models import (
    Equipment,
    Report,
    Sector,
    SubSector,
    TerritorialLocation,
)
from server.apps.hincal.services.enums import (
    TypeBusiness,
    TypeBusinessForCalculator,
    TypeTaxSystem,
)
from server.apps.hincal.services.validate_report import check_range
from server.apps.services.serializers import ModelSerializerWithPermission
from server.apps.support.api.serializers import (
    BaseOfferSerializer,
    BaseSupportSerializer,
)
from server.apps.support.models import Offer, Support


class ReportSerializer(ModelSerializerWithPermission):
    """Отчет."""

    supports = serializers.SerializerMethodField()
    offers = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta(object):
        model = Report
        fields = (
            'id',
            'user',
            'initial_data',
            'context',
            'supports',
            'offers',
            'tags',
            'permission_rules',
            'created_at',
            'updated_at',
        )

    def get_supports(self, report: Report):
        """Получаем возможные меры поддержки."""
        return BaseSupportSerializer(
            Support.objects.filter(
                tags__in=report.tags.all(),
                is_actual=True
            )[0:4],
            many=True,
        ).data

    def get_offers(self, report: Report):
        """Получаем возможные партнерские предложения по инвестированию."""
        return BaseOfferSerializer(
            Offer.objects.filter(
                tags__in=report.tags.all(),
            )[0:4],
            many=True,
        ).data


class CreateReportSerializer(serializers.Serializer):
    """Создание отчета."""

    type_business = serializers.ChoiceField(
        choices=TypeBusinessForCalculator.choices,
        required=True,
    )
    sector = serializers.PrimaryKeyRelatedField(
        queryset=Sector.objects.all(),
        required=True,
    )
    sub_sector = serializers.PrimaryKeyRelatedField(
        queryset=SubSector.objects.all(),
        required=False,
        allow_null=True,
    )
    from_staff = serializers.IntegerField(
        required=False,
        allow_null=True,
    )
    to_staff = serializers.IntegerField(
        required=False,
        allow_null=True,
    )
    territorial_locations = serializers.PrimaryKeyRelatedField(
        queryset=TerritorialLocation.objects.all(),
        many=True,
        required=False,
        allow_null=True,
    )
    from_land_area = serializers.IntegerField(
        required=False,
        allow_null=True,
    )
    to_land_area = serializers.IntegerField(
        required=False,
        allow_null=True,
    )
    properties = serializers.JSONField(
        allow_null=True,
        required=False,
        default=[],
    )
    equipments = serializers.PrimaryKeyRelatedField(
        queryset=Equipment.objects.all(),
        many=True,
        required=False,
        allow_null=True,
    )
    type_tax_system = serializers.ChoiceField(
        choices=TypeTaxSystem.choices,
        default=TypeTaxSystem.OSN,
    )
    need_accounting = serializers.BooleanField(default=False)
    need_registration = serializers.BooleanField(default=False)

    others = serializers.JSONField(
        allow_null=True,
        required=False,
        default=[],
    )

    def validate_type_tax_system(self, type_tax_system):
        """Валидация типа системы налогооблажения."""
        if type_tax_system not in TypeTaxSystem.values:
            raise ValidationError(
                {
                    'type_tax_system':
                        [_('Некорректная система налогооблажения')],
                },
            )
        return type_tax_system

    def validate(self, attrs):
        """Общая валидация.

        У юридического лица нет патентной системы налогооблажения.
        """
        type_business = attrs.get('type_business')
        type_tax_system = attrs.get('type_tax_system')
        if type_business == TypeBusiness.LEGAL and type_tax_system == TypeTaxSystem.PATENT:
            raise ValidationError(
                {
                    'type_tax_system':
                        [
                            _(
                                'У юридического лица нет патентной ' +
                                'системы налогооблажения',
                            ),
                        ],
                },
            )
        # Проверка диапазона по сотрудникам.
        attrs = check_range(
            attrs=attrs,
            from_name_value='from_staff',
            to_name_value='to_staff',
        )
        # Проверка диапазона по земле.
        attrs = check_range(
            attrs=attrs,
            from_name_value='from_land_area',
            to_name_value='to_land_area',
        )

        return attrs
