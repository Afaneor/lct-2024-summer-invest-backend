import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_message_format(
    api_client,
    message,
    message_format,
):
    """Формат Message."""
    url = reverse('api:personal-cabinet:message-detail', [message.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == message_format(message)


@pytest.mark.django_db()
def test_message_post(
    api_client,
):
    """Создание Message."""
    url = reverse('api:personal-cabinet:message-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_message_delete(api_client, message):
    """Удаление Message."""
    url = reverse('api:personal-cabinet:message-detail', [message.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_message_change(
    api_client,
    message,
):
    """Изменение Message."""
    url = reverse('api:personal-cabinet:message-detail', [message.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
