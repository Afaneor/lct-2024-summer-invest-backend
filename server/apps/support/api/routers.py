from rest_framework.routers import APIRootView

from server.apps.support.api.views import (
    ServiceProblemViewSet,
    ServiceSupportViewSet,
)
from server.apps.services.custom_router.api_router import ApiRouter


class ServiceSupportAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение для сервисов поддержки'
    name = 'service_support'


router = ApiRouter()

router.APIRootView = ServiceSupportAPIRootView
router.register('service-problems', ServiceProblemViewSet, 'service-problems')
router.register('service-supports', ServiceSupportViewSet, 'service-supports')
