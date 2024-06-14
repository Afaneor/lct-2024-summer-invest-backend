import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_event_format(
    api_client,
    event,
    event_format,
):
    """Формат Event."""
    url = reverse('service-interaction:event-detail', [event.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == event_format(event)


@pytest.mark.django_db()
def test_event_post(
    api_client,
):
    """Создание Event."""
    url = reverse('service-interaction:event-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_event_delete(api_client, event):
    """Удаление Event."""
    url = reverse('service-interaction:event-detail', [event.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_event_change(
    api_client,
    event,
):
    """Изменение Event."""
    url = reverse('api:service-interaction:event-detail', [event.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
