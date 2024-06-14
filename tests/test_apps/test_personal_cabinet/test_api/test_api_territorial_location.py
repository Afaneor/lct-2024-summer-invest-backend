import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_territorial_location_format(
    api_client,
    territorial_location,
    territorial_location_format,
):
    """Формат TerritorialLocation."""
    url = reverse('personal-cabinet:territorial-location-detail', [territorial_location.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == territorial_location_format(territorial_location)


@pytest.mark.django_db()
def test_territorial_location_post(
    api_client,
):
    """Создание TerritorialLocation."""
    url = reverse('personal-cabinet:territorial-location-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_territorial_location_delete(api_client, territorial_location):
    """Удаление TerritorialLocation."""
    url = reverse('personal-cabinet:territorial-location-detail', [territorial_location.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_territorial_location_change(
    api_client,
    territorial_location,
):
    """Изменение TerritorialLocation."""
    url = reverse('api:personal-cabinet:territorial-location-detail', [territorial_location.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
