import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_sector_format(
    api_client,
    sector,
    sector_format,
):
    """Формат Sector."""
    url = reverse('api:personal-cabinet:sectors-detail', [sector.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        sector_format(sector)
    )


@pytest.mark.django_db()
def test_sector_list(
    api_client,
):
    """Список Sector."""
    url = reverse('api:personal-cabinet:sectors-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
