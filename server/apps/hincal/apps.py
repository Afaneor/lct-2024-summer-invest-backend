from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HincalConfig(AppConfig):
    """Конфиг приложения "Russian name project"."""

    name = 'server.apps.hincal'
    label = 'hincal'
    verbose_name = _('Инвестиционный калькулятор')

    def ready(self) -> None:
        """Подключение прав происходит при подключении app."""
        import server.apps.hincal.api.routers
        import server.apps.hincal.permissions
