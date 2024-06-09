from rest_framework.routers import APIRootView

from server.apps.service_interaction.api.views import (
    CommentViewSet,
    EventViewSet,
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
router.register('comments', CommentViewSet, 'comments')
router.register('posts', PostViewSet, 'posts')
router.register('topics', TopicViewSet, 'topics')
