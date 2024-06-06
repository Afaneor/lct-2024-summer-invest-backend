from django.contrib import admin

from server.apps.personal_cabinet.models import (
    Business,
    Message,
    Sector,
    SelectedInvestmentObject,
    SelectionRequest,
    SubSector,
    TerritorialLocation,
)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin[Business]):
    """Бизнес.

    Компании и ИП получаются из DaData.
    Физическое лицо заполняет данные руками.
    """

    list_display = (
        'id',
        'user',
        'type_business',
        'inn',
        'sector',
        'short_business_name',
    )

    list_filter = (
        'type_business',
        'sector',
        'sub_sector',
    )
    search_fields = (
        'user__email',
        'user__first_name',
        'user_last_name',
        'sector',
        'short_business_name',
        'full_business_name',
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
    ordering = (
        'id',
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin[Message]):
    """Сообщение."""

    list_display = (
        'id',
        'owner_type',
        'selection_request',
        'parent',
    )
    list_filter = (
        'owner_type',
    )
    search_fields = (
        'text',
        'selection_request__user__username',
        'selection_request__user__email',
        'selection_request__user__first_name',
        'selection_request__user__last_name',
        'selection_request__investment_objects__name',
    )
    ordering = (
        'id',
    )


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin[Sector]):
    """Сектор."""

    list_display = (
        'id',
        'name',
        'slug',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
    )


@admin.register(SelectedInvestmentObject)
class SelectedInvestmentObjectAdmin(admin.ModelAdmin[SelectedInvestmentObject]):
    """Подобранный инвестиционный объект."""

    list_display = (
        'id',
        'investment_object',
        'selection_request',
        'message',
        'is_relevant',
    )
    list_filter = (
        'is_relevant',
    )
    search_fields = (
        'investment_object__name',
        'selection_request__user__username',
        'selection_request__user__email',
        'selection_request__user__first_name',
        'selection_request__user__last_name',
    )
    ordering = (
        'id',
    )


@admin.register(SelectionRequest)
class SelectionRequestObjectAdmin(admin.ModelAdmin[SelectionRequest]):
    """Запрос на подбор."""

    list_display = (
        'id',
        'user',
        'anonymous_user_id',
        'is_actual',
    )
    list_filter = (
        'is_actual',
    )
    search_fields = (
        'anonymous_user_id',
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'investment_objects__name',
    )
    ordering = (
        'id',
    )


@admin.register(SubSector)
class SubSectorAdmin(admin.ModelAdmin[SubSector]):
    """Сектор."""

    list_display = (
        'id',
        'name',
        'slug',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
    )


@admin.register(TerritorialLocation)
class TerritorialLocationAdmin(admin.ModelAdmin[TerritorialLocation]):
    """Территориальное расположение."""

    list_display = (
        'id',
        'shot_name',
        'full_name',
        'slug',
    )
    search_fields = (
        'slug',
        'shot_name',
        'full_name',
    )
    ordering = (
        'id',
    )
