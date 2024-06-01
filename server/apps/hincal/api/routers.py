from rest_framework.routers import APIRootView

from server.apps.hincal.api.views import (
    ArchiveViewSet,
    BusinessIndicatorViewSet,
    BusinessViewSet,
    EquipmentViewSet,
    ReportViewSet,
    SectorViewSet,
    StatisticViewSet,
    SubSectorViewSet,
    TerritorialLocationViewSet,
)
from server.apps.services.custom_router.api_router import ApiRouter


class HincalAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение Hincal'
    name = 'hincal'


router = ApiRouter()

router.APIRootView = HincalAPIRootView
router.register('archives', ArchiveViewSet, 'archives')
router.register('businesses', BusinessViewSet, 'businesses')
router.register('statistics', StatisticViewSet, 'statistics')
router.register('business-indicator', BusinessIndicatorViewSet, 'business-indicator')
router.register('equipments', EquipmentViewSet, 'equipments')
router.register('reports', ReportViewSet, 'reports')
router.register('sectors', SectorViewSet, 'sectors')
router.register('sub-sectors', SubSectorViewSet, 'sub-sectors')
router.register(
    'territorial-location',
    TerritorialLocationViewSet,
    'territorial-location',
)
