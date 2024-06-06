from server.apps.investment_object.api.views.investment_object import (
    InvestmentObjectViewSet,
)
from server.apps.investment_object.api.views.tender import TenderViewSet
from server.apps.investment_object.api.views.tender_lot import TenderLotViewSet

__all__ = [
    InvestmentObjectViewSet,
    TenderViewSet,
    TenderLotViewSet,
]
