from rest_framework import serializers

from server.apps.personal_cabinet.models import (
    Business,
    Message,
    Sector,
    SubSector,
    TerritorialLocation,
)


class BaseSectorSerializer(serializers.ModelSerializer):
    """
    Сериалайзер оборудования. Используется во вложенных сериалайзерах.
    """

    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
        )


class BaseSubSectorSerializer(serializers.ModelSerializer):
    """
    Базовая информация о подотрасли. Используется во вложенных сериалайзерах.
    """

    class Meta:
        model = SubSector
        fields = (
            'id',
            'name',
        )


class BaseTerritorialLocationSerializer(serializers.ModelSerializer):
    """Сериалайзер территориального расположения для других сериализаторов."""

    class Meta:
        model = TerritorialLocation
        fields = (
            'id',
            'short_name',
            'full_name',
        )


class BaseBusinessSerializer(serializers.ModelSerializer):
    """
    Сериалайзер бизнеса. Используется во вложенных сериалайзерах.
    """

    territorial_location = BaseTerritorialLocationSerializer()
    sector = BaseSectorSerializer()
    sub_sector = BaseSubSectorSerializer()
    business_type_label = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = (
            'business_type',
            'business_type_label',
            'inn',
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
        )

    def get_business_type_label(
        self,
        business: Business,
    ):
        """Подпись к business_type."""
        return business.get_business_type_display()


class BaseMessageSerializer(serializers.ModelSerializer):
    """
    Сериалайзер сообщения. Используется во вложенных сериалайзерах.
    """

    owner_type_label = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = (
            'id',
            'owner_type',
            'selection_request',
            'text',
            'user_filter',
            'bot_filter',
            'parent',
            'created_at',
            'owner_type_label',
        )

    def get_owner_type_label(
        self,
        message: Message,
    ):
        """Подпись к owner_type."""
        return message.get_owner_type_display()
