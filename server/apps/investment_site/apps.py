from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvestmentSiteConfig(AppConfig):
    """Конфиг приложения "Russian name project"."""

    name = 'server.apps.investment_site'
    verbose_name = _('Инвестиционные площадки')

    def ready(self) -> None:
        """Подключение прав происходит при подключении app."""
        import server.apps.investment_site.api.routers
        import server.apps.investment_site.permissions
