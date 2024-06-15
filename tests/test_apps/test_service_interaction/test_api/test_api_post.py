import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_post_format(
    api_client,
    post,
    post_format,
):
    """Формат Post."""
    url = reverse('api:service-interaction:posts-detail', [post.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        post_format(post)
    )


@pytest.mark.django_db()
def test_post_post(
    user_api_client,
    topic,
):
    """Создание Post."""
    url = reverse('api:service-interaction:posts-list')
    response = user_api_client.post(
        url,
        data={
            'topic': topic.id,
            'text': 'тест'
        },
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_post_list(api_client):
    """Удаление Post."""
    url = reverse('api:service-interaction:posts-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

