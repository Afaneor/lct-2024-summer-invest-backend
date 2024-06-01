from rest_framework.routers import APIRootView

from server.apps.investment_site.api.views import (
    InvestmentSiteViewSet,
    TenderLotViewSet,
    TenderViewSet,
)
from server.apps.services.custom_router.api_router import ApiRouter


class InvestmentSiteAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение для инвестиционных площадок'
    name = 'investment_site'


router = ApiRouter()

router.APIRootView = InvestmentSiteAPIRootView
router.register('investment-sites', InvestmentSiteViewSet, 'investment-sites')
router.register('tenders', TenderViewSet, 'tenders')
router.register('tender-lots', TenderLotViewSet, 'tender-lots')
