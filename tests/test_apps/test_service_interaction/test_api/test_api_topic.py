import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_topic_format(
    api_client,
    topic,
    topic_format,
):
    """Формат Topic."""
    url = reverse('service-interaction:topic-detail', [topic.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == topic_format(topic)


@pytest.mark.django_db()
def test_topic_post(
    api_client,
):
    """Создание Topic."""
    url = reverse('service-interaction:topic-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_topic_delete(api_client, topic):
    """Удаление Topic."""
    url = reverse('service-interaction:topic-detail', [topic.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_topic_change(
    api_client,
    topic,
):
    """Изменение Topic."""
    url = reverse('api:service-interaction:topic-detail', [topic.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
