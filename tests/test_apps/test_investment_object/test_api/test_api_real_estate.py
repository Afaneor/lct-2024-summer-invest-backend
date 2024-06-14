import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import response_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_real_estate_detail(
    api_client,
    real_estate,
    real_estate_format,
):
    """Формат RealEstate."""
    url = reverse(
        'api:investment-object:real-estates-detail',
        [real_estate.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        response_without_keys(response.json()) ==
        real_estate_format(real_estate)
    )


@pytest.mark.django_db()
def test_real_estate_list(
    api_client,
):
    """Список RealEstate."""
    url = reverse('api:investment-object:real-estates-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
