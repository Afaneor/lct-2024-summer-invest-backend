import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_comment_format(
    api_client,
    comment,
    comment_format,
):
    """Формат Comment."""
    url = reverse('service-interaction:comment-detail', [comment.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == comment_format(comment)


@pytest.mark.django_db()
def test_comment_post(
    api_client,
):
    """Создание Comment."""
    url = reverse('service-interaction:comment-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_comment_delete(api_client, comment):
    """Удаление Comment."""
    url = reverse('service-interaction:comment-detail', [comment.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_comment_change(
    api_client,
    comment,
):
    """Изменение Comment."""
    url = reverse('api:service-interaction:comment-detail', [comment.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
