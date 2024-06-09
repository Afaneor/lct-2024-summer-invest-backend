from rest_framework.routers import APIRootView

from server.apps.service_interaction.api.views import (
    EventViewSet,
    FeedbackViewSet,
    PostViewSet,
    TopicViewSet,
)
from server.apps.services.custom_router.api_router import ApiRouter


class ServiceInteractionAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = 'Приложение персонального кабинета пользователя'
    name = 'personal_cabinet'


router = ApiRouter()

router.APIRootView = ServiceInteractionAPIRootView
router.register('events', EventViewSet, 'events')
router.register('feedbacks', FeedbackViewSet, 'feedbacks')
router.register('posts', PostViewSet, 'posts')
router.register('topics', TopicViewSet, 'topics')
