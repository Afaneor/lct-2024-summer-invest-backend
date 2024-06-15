import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_event_format(
    api_client,
    event,
    event_format,
):
    """Формат Event."""
    url = reverse('api:service-interaction:events-detail', [event.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        event_format(event)
    )


@pytest.mark.django_db()
def test_event_list(
    api_client,
):
    """Список Event."""
    url = reverse('api:service-interaction:events-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
