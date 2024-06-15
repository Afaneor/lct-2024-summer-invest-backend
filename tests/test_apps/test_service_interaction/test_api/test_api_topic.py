import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_topic_format(
    api_client,
    topic,
    topic_format,
):
    """Формат Topic."""
    url = reverse('api:service-interaction:topics-detail', [topic.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        topic_format(topic)
    )


@pytest.mark.django_db()
def test_topic_list(
    api_client,
):
    """Список Topic."""
    url = reverse('api:service-interaction:topics-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
