"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from health_check import urls as health_urls

from server.apps.blog.api.routers import router as blog_router
from server.apps.hincal.api.routers import router as hincal_router
from server.apps.services.custom_router.api_router import router
from server.apps.support.api.routers import router as support_router
from server.apps.user.api.routers import router as user_router
from server.url_components import (
    admin_urlpatterns,
    docs_urlpatterns,
    jwt_urlpatterns,
    seo_urlpatterns,
)

# Регистрируем routers приложений.
router.register('blog', blog_router, 'blog')
router.register('hincal', hincal_router, 'hincal')
router.register('user', user_router, 'user')
router.register('support', support_router, 'support')

api_url = [
    path('api/', include((router.urls, 'api'))),
]

admin.autodiscover()

urlpatterns = [
    # Health checks:
    path('health/', include(health_urls)),  # noqa: DJ05
    path('api-auth/', include('rest_framework.urls')),
    path('', include(api_url)),

    *admin_urlpatterns,
    *docs_urlpatterns,
    *jwt_urlpatterns,
    *seo_urlpatterns,
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = (
        [
            # URLs specific only to django-debug-toolbar:
            path('__debug__/', include(debug_toolbar.urls)),  # noqa: DJ05
        ] + urlpatterns +
        static(
            # Serving media files in development only:
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    )
