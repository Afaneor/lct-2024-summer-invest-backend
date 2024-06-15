from locust import HttpUser, task


class CheckApp(HttpUser):
    """Проверка нагрузки."""

    headers = {'Authorization': 'Token 1234'}

    @task
    def check_user_info(self):
        """Информация о пользователе."""
        self.client.get(
            '/api/accounts/account/get-info/',
            headers=self.headers,
        )
        self.client.get(
            '/api/accounts/customization/get-customization/',
            headers=self.headers,
        )

    @task
    def list_notification(self):
        """Уведомления."""
        self.client.get(
            '/api/notifications/notification/',
            headers=self.headers,
        )

    @task
    def retrieve_measure(self):
        """Рекомендации замера."""
        self.client.get(
            '/api/health/measure/',
            headers=self.headers,
        )
        self.client.get(
            '/api/health/measure-recommendation/',
            headers=self.headers,
        )
        self.client.get(
            '/api/health/measure/assembled/',
            headers=self.headers,
        )

    @task
    def news(self):
        """Новости."""
        self.client.get(
            '/api/news/post/',
            headers=self.headers,
        )

    @task
    def export_ecg(self):
        """Экспорт ЭКГ."""
        response = self.client.get(
            '/api/health/measure/',
            headers=self.headers,
        )
        if response.status_code == 200:  # noqa: WPS432
            measure_id = response.json()['results'][0]['id']
            self.client.get(
                f'/api/health/measure/{measure_id}',
                headers=self.headers,
            )
            self.client.get(
                f'/api/health/measure/{measure_id}/export-ecg-pdf',
                headers=self.headers,
            )
