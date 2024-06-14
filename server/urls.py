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

from server.apps.investment_object.api.routers import (
    router as investment_object_router,
)
from server.apps.personal_cabinet.api.routers import (
    router as personal_cabinet_router,
)
from server.apps.service_interaction.api.routers import (
    router as service_interaction_router,
)
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
router.register('investment-object', investment_object_router, 'investment-object')
router.register('personal-cabinet', personal_cabinet_router, 'personal-cabinet')
router.register('service-interactions', service_interaction_router, 'service-interactions')
router.register('support', support_router, 'support')
router.register('user', user_router, 'user')

api_url = [
    path("api/", include((router.urls, "api"))),
]

admin.autodiscover()

urlpatterns = [
    # Health checks:
    path('api-auth/', include('rest_framework.urls')),
    path('health/', include(health_urls)),  # noqa: DJ05
    path("", include(api_url)),
    path(r'admin_tools/', include('admin_tools.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
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
