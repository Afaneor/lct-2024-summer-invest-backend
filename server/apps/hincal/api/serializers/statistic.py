from rest_framework import serializers


class AllStatisticSerializer(serializers.Serializer):
    """Общая статистика по системе."""

    popular_sector = serializers.ListSerializer(
        child=serializers.DictField(),
        required=False,
        allow_null=True,
    )
    average_investment_amount_bi = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    average_investment_amount_math = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    total_investment_amount_bi = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    total_investment_amount_math = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    number_of_reports = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    number_of_business = serializers.FloatField(
        required=False,
        allow_null=True,
    )


class UserStatisticSerializer(serializers.Serializer):
    """Общая статистика по пользователю."""

    popular_sector = serializers.ListSerializer(
        child=serializers.DictField(),
        required=False,
        allow_null=True,
    )
    average_investment_amount_bi = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    average_investment_amount_math = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    total_investment_amount_bi = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    total_investment_amount_math = serializers.FloatField(
        required=False,
        allow_null=True,
    )
    number_of_reports = serializers.FloatField(
        required=False,
        allow_null=True,
    )
