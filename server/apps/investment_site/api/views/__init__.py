from server.apps.investment_site.api.views.investment_site import (
    InvestmentSiteViewSet,
)
from server.apps.investment_site.api.views.tender import TenderViewSet
from server.apps.investment_site.api.views.tender_lot import TenderLotViewSet

__all__ = [
    InvestmentSiteViewSet,
    TenderViewSet,
    TenderLotViewSet,
]
