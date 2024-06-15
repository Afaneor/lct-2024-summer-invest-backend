from locust import HttpUser, task


class CheckApp(HttpUser):
    """Проверка нагрузки."""

    @task
    def investment_objects(self):
        """Информация о пользователе."""
        self.client.get(
            'api/investment-object/investment-objects/',
        )

    @task
    def service_suppoer(self):
        """Уведомления."""
        self.client.get(
            'api/support/service-supports/',
        )

    @task
    def retrieve_measure(self):
        """Рекомендации замера."""
        self.client.get(
            'api/support/service-supports/additional-data/',
        )
