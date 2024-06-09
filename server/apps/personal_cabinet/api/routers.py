from rest_framework.routers import APIRootView

from server.apps.personal_cabinet.api.views import (
    BusinessViewSet,
    MessageViewSet,
    SectorViewSet,
    SelectedEntityViewSet,
    SelectionRequestViewSet,
    SubSectorViewSet,
    TerritorialLocationViewSet,
)
from server.apps.services.custom_router.api_router import ApiRouter


class PersonalCabinetAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение персонального кабинета пользователя'
    name = 'personal_cabinet'


router = ApiRouter()

router.APIRootView = PersonalCabinetAPIRootView
router.register('businesses', BusinessViewSet, 'businesses')
router.register('sectors', SectorViewSet, 'sectors')
router.register('sub-sectors', SubSectorViewSet, 'sub-sectors')
router.register(
    'territorial-location',
    TerritorialLocationViewSet,
    'territorial-location',
)
router.register('selection-requests', SelectionRequestViewSet, 'selection-requests')
router.register('messages', MessageViewSet, 'messages')
router.register(
    'selected-investment-objects',
    SelectedEntityViewSet,
    'selected-investment-objects',
)
