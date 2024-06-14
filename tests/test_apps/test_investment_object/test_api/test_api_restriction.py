import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_restriction_format(
    api_client,
    restriction,
    restriction_format,
):
    """Формат Restriction."""
    url = reverse('investment-object:restriction-detail', [restriction.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == restriction_format(restriction)


@pytest.mark.django_db()
def test_restriction_post(
    api_client,
):
    """Создание Restriction."""
    url = reverse('investment-object:restriction-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_restriction_delete(api_client, restriction):
    """Удаление Restriction."""
    url = reverse('investment-object:restriction-detail', [restriction.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_restriction_change(
    api_client,
    restriction,
):
    """Изменение Restriction."""
    url = reverse('api:investment-object:restriction-detail', [restriction.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
