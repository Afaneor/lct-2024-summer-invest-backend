from django.contrib import admin

from server.apps.investment_site.models import (
    InvestmentSite,
    Tender,
    TenderLot,
)


@admin.register(InvestmentSite)
class InvestmentSiteAdmin(admin.ModelAdmin[InvestmentSite]):
    """Инвестиционная площадка."""

    list_display = (
        'id',
        'investment_site_id',
        'name',
        'investment_object_type',
        'detail_url',
    )
    list_filter = (
        'investment_object_type',
    )
    search_fields = (
        'investment_site_id',
        'name',
        'investment_object_type',
        'detail_url',
    )
    ordering = (
        'id',
    )


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin[Tender]):
    """Тендер."""

    list_display = (
        'id',
        'tender_id',
        'bidding_type',
        'detail_url',
    )
    list_filter = (
        'bidding_type',
    )
    search_fields = (
        'tender_id',
        'bidding_type',
        'detail_url',
    )
    ordering = (
        'id',
    )


@admin.register(TenderLot)
class TenderLotAdmin(admin.ModelAdmin[TenderLot]):
    """Лот тендера."""

    list_display = (
        'id',
        'tender',
        'tender_lot_id',
        'name',
        'detail_url',
    )
    list_filter = (
        'tender__bidding_type',
    )
    search_fields = (
        'tender_lot_id',
        'name',
        'detail_url',
    )
    ordering = (
        'id',
    )
