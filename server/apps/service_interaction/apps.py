from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InteractionConfig(AppConfig):
    """Конфиг приложения для сервиса взаимодействия."""

    name = 'server.apps.service_interaction'
    label = 'service_interaction'
    verbose_name = _('Сервис взаимодействия')

    def ready(self):
        """Подключение роутера и прав происходит при подключении app."""
        super().ready()
        import server.apps.service_interaction.api.routers
        import server.apps.service_interaction.permissions

