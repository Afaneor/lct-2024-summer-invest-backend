from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    """Конфигурация приложения."""

    name = 'server.apps.blog'
    label = 'blog'
    verbose_name = _('Блог')

    def ready(self) -> None:
        """Подключение прав происходит при подключении app."""
        super().ready()
        import server.apps.blog.api.routers
        import server.apps.blog.permissions
