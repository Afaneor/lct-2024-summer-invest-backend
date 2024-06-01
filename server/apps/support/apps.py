from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    """Конфигурация приложения."""

    name = 'server.apps.support'
    label = 'support'
    verbose_name = _('Поддержка')

    def ready(self) -> None:
        """Подключение прав происходит при подключении app."""
        super().ready()
        import server.apps.support.api.routers
        import server.apps.support.permissions
