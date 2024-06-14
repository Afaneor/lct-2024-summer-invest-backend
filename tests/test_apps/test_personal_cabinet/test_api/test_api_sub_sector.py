import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_sub_sector_format(
    api_client,
    sub_sector,
    sub_sector_format,
):
    """Формат SubSector."""
    url = reverse('personal-cabinet:sub-sector-detail', [sub_sector.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == sub_sector_format(sub_sector)


@pytest.mark.django_db()
def test_sub_sector_post(
    api_client,
):
    """Создание SubSector."""
    url = reverse('personal-cabinet:sub-sector-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_sub_sector_delete(api_client, sub_sector):
    """Удаление SubSector."""
    url = reverse('personal-cabinet:sub-sector-detail', [sub_sector.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_sub_sector_change(
    api_client,
    sub_sector,
):
    """Изменение SubSector."""
    url = reverse('api:personal-cabinet:sub-sector-detail', [sub_sector.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
