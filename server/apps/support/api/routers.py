from rest_framework.routers import APIRootView

from server.apps.services.custom_router.api_router import ApiRouter
from server.apps.support.api.views import (
    ProblemCategoryViewSet,
    ServiceSupportViewSet,
)


class ServiceSupportAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение для сервисов поддержки'
    name = 'service_support'


router = ApiRouter()

router.APIRootView = ServiceSupportAPIRootView
router.register('problem-categories', ProblemCategoryViewSet, 'problem-categories')
router.register('service-supports', ServiceSupportViewSet, 'service-supports')
