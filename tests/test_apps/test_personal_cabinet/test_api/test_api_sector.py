import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_sector_format(
    api_client,
    sector,
    sector_format,
):
    """Формат Sector."""
    url = reverse('personal-cabinet:sector-detail', [sector.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == sector_format(sector)


@pytest.mark.django_db()
def test_sector_post(
    api_client,
):
    """Создание Sector."""
    url = reverse('personal-cabinet:sector-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_sector_delete(api_client, sector):
    """Удаление Sector."""
    url = reverse('personal-cabinet:sector-detail', [sector.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_sector_change(
    api_client,
    sector,
):
    """Изменение Sector."""
    url = reverse('api:personal-cabinet:sector-detail', [sector.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
