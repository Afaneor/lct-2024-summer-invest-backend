import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_privilege_format(
    api_client,
    privilege,
    privilege_format,
):
    """Формат Privilege."""
    url = reverse('investment-object:privilege-detail', [privilege.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == privilege_format(privilege)


@pytest.mark.django_db()
def test_privilege_post(
    api_client,
):
    """Создание Privilege."""
    url = reverse('investment-object:privilege-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_privilege_delete(api_client, privilege):
    """Удаление Privilege."""
    url = reverse('investment-object:privilege-detail', [privilege.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_privilege_change(
    api_client,
    privilege,
):
    """Изменение Privilege."""
    url = reverse('api:investment-object:privilege-detail', [privilege.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
