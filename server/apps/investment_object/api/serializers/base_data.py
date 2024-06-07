from rest_framework import serializers

from server.apps.investment_object.models import (
    EconomicActivity,
    InvestmentObject,
    Privilege,
    ReadyBusiness,
)


class BaseEconomicActivitySerializer(serializers.ModelSerializer):
    """Базовый сериалайзер экономической деятельности."""

    class Meta:
        model = EconomicActivity
        fields = (
            'id',
            'code',
            'name',
        )


class BaseInfrastructureSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер инфраструктуры."""

    class Meta:
        model = EconomicActivity
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
        )


class BaseInvestmentObjectSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер инвестиционных площадок."""

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
        )


class BasePrivilegeSerializer(serializers.ModelSerializer):
    """Сериалайзер льгот."""

    class Meta:
        model = Privilege
        fields = (
            'id',
            'name',
        )


class BaseReadyBusinessSerializer(serializers.ModelSerializer):
    """Сериалайзер готового бизнеса."""

    class Meta:
        model = ReadyBusiness
        fields = (
            'id',
            'external_id',
            'name',
            'description',
            'extra_data',
        )
