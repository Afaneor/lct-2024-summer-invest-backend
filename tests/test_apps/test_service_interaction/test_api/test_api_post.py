import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_post_format(
    api_client,
    post,
    post_format,
):
    """Формат Post."""
    url = reverse('service-interaction:post-detail', [post.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == post_format(post)


@pytest.mark.django_db()
def test_post_post(
    api_client,
):
    """Создание Post."""
    url = reverse('service-interaction:post-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_post_delete(api_client, post):
    """Удаление Post."""
    url = reverse('service-interaction:post-detail', [post.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_post_change(
    api_client,
    post,
):
    """Изменение Post."""
    url = reverse('api:service-interaction:post-detail', [post.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
