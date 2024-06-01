"""Файл для router."""
from django.utils.translation import gettext_lazy as _
from rest_framework.routers import APIRootView

from server.apps.blog.api.views import PostViewSet
from server.apps.services.custom_router.api_router import ApiRouter


class BlogAPIRootView(APIRootView):
    """Корневой view для апи."""

    __doc__ = _('Приложение блога')
    name = _('Блог')


router = ApiRouter()
router.APIRootView = BlogAPIRootView

router.register('posts', PostViewSet, 'posts')
