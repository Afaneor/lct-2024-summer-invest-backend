from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PersonalCabinetConfig(AppConfig):
    """Конфиг приложения с персональным кабинетом."""

    name = 'server.apps.personal_cabinet'
    label = 'personal_cabinet'
    verbose_name = _('Персональный кабинет')

    def ready(self):
        """Подключение роутера и прав происходит при подключении app."""
        super().ready()
        import server.apps.personal_cabinet.api.routers
        import server.apps.personal_cabinet.permissions

