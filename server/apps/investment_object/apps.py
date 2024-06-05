from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvestmentSiteConfig(AppConfig):
    """Конфиг приложения "Russian name project"."""

    name = 'server.apps.investment_object'
    verbose_name = _('Инвестиционные площадки')

    def ready(self) -> None:
        """Подключение прав происходит при подключении app."""
        import server.apps.investment_object.api.routers
        import server.apps.investment_object.permissions
