import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_user_format(
    api_client,
    user,
    user_format,
):
    """Формат User."""
    url = reverse('user:user-detail', [user.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == user_format(user)


@pytest.mark.django_db()
def test_user_post(
    api_client,
):
    """Создание User."""
    url = reverse('user:user-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_user_delete(api_client, user):
    """Удаление User."""
    url = reverse('user:user-detail', [user.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_user_change(
    api_client,
    user,
):
    """Изменение User."""
    url = reverse('api:user:user-detail', [user.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
