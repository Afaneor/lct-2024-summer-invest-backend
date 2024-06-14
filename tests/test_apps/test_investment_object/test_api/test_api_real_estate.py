import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_real_estate_format(
    api_client,
    real_estate,
    real_estate_format,
):
    """Формат RealEstate."""
    url = reverse('investment-object:real-estate-detail', [real_estate.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == real_estate_format(real_estate)


@pytest.mark.django_db()
def test_real_estate_post(
    api_client,
):
    """Создание RealEstate."""
    url = reverse('investment-object:real-estate-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_real_estate_delete(api_client, real_estate):
    """Удаление RealEstate."""
    url = reverse('investment-object:real-estate-detail', [real_estate.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_real_estate_change(
    api_client,
    real_estate,
):
    """Изменение RealEstate."""
    url = reverse('api:investment-object:real-estate-detail', [real_estate.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
