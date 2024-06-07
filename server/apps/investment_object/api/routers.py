from rest_framework.routers import APIRootView

from server.apps.investment_object.api.views import (
    EconomicActivityViewSet,
    InfrastructureViewSet,
    InvestmentObjectViewSet,
    PrivilegeViewSet,
    ReadyBusinessViewSet,
    RealEstateViewSet,
    RestrictionViewSet,
    SpecializedSiteViewSet,
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
router.register(
    'economic-activities',
    EconomicActivityViewSet,
    'economic-activities',
)
router.register(
    'infrastructures',
    InfrastructureViewSet,
    'infrastructures',
)
router.register('privileges', PrivilegeViewSet, 'privilege')
router.register('ready-businesses', ReadyBusinessViewSet, 'ready-businesses')
router.register(
    'investment-objects',
    InvestmentObjectViewSet,
    'investment-objects',
)
router.register('real-estates', RealEstateViewSet, 'real-estates')
router.register('restrictions', RestrictionViewSet, 'restrictions')
router.register(
    'specialized-sites',
    SpecializedSiteViewSet,
    'specialized-sites',
)
router.register('tenders', TenderViewSet, 'tenders')
router.register('tender-lots', TenderLotViewSet, 'tender-lots')
