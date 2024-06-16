from django.contrib import admin

from server.apps.investment_object.models import (
    EconomicActivity,
    Infrastructure,
    InvestmentObject,
    Privilege,
    ReadyBusiness,
    RealEstate,
    Restriction,
    SpecializedSite,
    TenderLot,
    TransactionForm,
)


@admin.register(InvestmentObject)
class InvestmentObjectAdmin(admin.ModelAdmin[InvestmentObject]):
    """Инвестиционная площадка."""

    list_display = (
        'id',
        'name',
        'object_type',
        'url',
    )
    list_filter = (
        'object_type',
    )
    search_fields = (
        'name',
        'object_type',
        'url',
    )
    ordering = (
        'id',
    )


@admin.register(TenderLot)
class TenderLotAdmin(admin.ModelAdmin[TenderLot]):
    """Лот тендера."""

    list_display = (
        'id',
        'external_id',
    )
    search_fields = (
        'external_id',
    )
    ordering = (
        'id',
    )


@admin.register(EconomicActivity)
class EconomicActivityAdmin(admin.ModelAdmin[EconomicActivity]):
    """Экономическая деятельность."""

    list_display = (
        'id',
        'code',
        'section',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'section'
    )
    ordering = (
        'id',
    )


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin[Infrastructure]):
    """Инфраструктура."""

    list_display = (
        'id',
        'name',
        'availability',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'availability'
    )
    ordering = (
        'id',
    )


@admin.register(Privilege)
class PrivilegeAdmin(admin.ModelAdmin[Privilege]):
    """Льгота."""

    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
    )


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin[RealEstate]):
    """Недвижимость."""

    list_display = (
        'id',
        'investment_object',
    )
    search_fields = (
        'investment_object__name',
    )
    list_filter = (
        'preferential_treatment',
    )
    ordering = (
        'id',
    )


@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin[Restriction]):
    """Ограничения по видам деятельности."""

    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'id',
    )


@admin.register(SpecializedSite)
class SpecializedSiteAdmin(admin.ModelAdmin[SpecializedSite]):
    """Специализированная площадка."""

    list_display = (
        'id',
        'investment_object',
    )
    search_fields = (
        'investment_object__name',
    )
    ordering = (
        'id',
    )


@admin.register(ReadyBusiness)
class ReadyBusinessAdmin(admin.ModelAdmin[ReadyBusiness]):
    """Готовый бизнес."""

    list_display = (
        'id',
        'investment_object',
    )
    search_fields = (
        'investment_object__name',
    )
    ordering = (
        'id',
    )


@admin.register(TransactionForm)
class TransactionFormAdmin(admin.ModelAdmin[TransactionForm]):
    """Форма сделки."""

    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'transaction_form_type',
    )
    ordering = (
        'id',
    )
