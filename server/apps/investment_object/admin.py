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
)


@admin.register(InvestmentObject)
class InvestmentObjectAdmin(admin.ModelAdmin[InvestmentObject]):
    """Инвестиционная площадка."""

    list_display = (
        'id',
        'external_id',
        'name',
        'object_type',
        'url',
    )
    list_filter = (
        'object_type',
    )
    search_fields = (
        'external_id',
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
        'tender_lot_id',
        'url',
    )
    list_filter = (
        # 'transaction_form',
    )
    search_fields = (
        'tender_lot_id',
        'url',
    )
    ordering = (
        'id',
    )


admin.site.register(EconomicActivity)
admin.site.register(Infrastructure)
admin.site.register(Privilege)
admin.site.register(RealEstate)
admin.site.register(Restriction)
admin.site.register(SpecializedSite)
admin.site.register(ReadyBusiness)
