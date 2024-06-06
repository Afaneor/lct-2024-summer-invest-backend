from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SupportConfig(AppConfig):
    """Конфиг приложения поддержки."""

    name = 'server.apps.support'
    verbose_name = _('Поддержка')

    def ready(self) -> None:
        """Подключение прав происходит при подключении app."""
        import server.apps.support.api.routers

        # import server.apps.support.permissions
