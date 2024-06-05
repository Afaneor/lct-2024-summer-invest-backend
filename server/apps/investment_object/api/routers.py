from rest_framework.routers import APIRootView

from server.apps.investment_object.api.views import (
    InvestmentObjectViewSet,
    TenderLotViewSet,
    TenderViewSet,
)
from server.apps.services.custom_router.api_router import ApiRouter


class InvestmentSiteAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение для инвестиционных площадок'
    name = 'investment_object'


router = ApiRouter()

router.APIRootView = InvestmentSiteAPIRootView
router.register('investment-objects', InvestmentObjectViewSet, 'investment-objects')
router.register('tenders', TenderViewSet, 'tenders')
router.register('tender-lots', TenderLotViewSet, 'tender-lots')
