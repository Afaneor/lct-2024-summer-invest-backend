import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_message_format(
    api_client,
    message,
    message_format,
):
    """Формат Message."""
    url = reverse('api:personal-cabinet:messages-detail', [message.id])

    response = api_client.get(
        url,
        headers={
            'GENERATED-USER-ID': 'test-anonymous-user-id'
        }
    )

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        message_format(message)
    )


@pytest.mark.django_db()
def test_message_list(api_client):
    """Список Message."""
    url = reverse('api:personal-cabinet:messages-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
