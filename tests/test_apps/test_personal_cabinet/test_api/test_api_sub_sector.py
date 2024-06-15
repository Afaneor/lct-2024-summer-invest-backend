import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_sub_sector_detail(
    api_client,
    sub_sector,
    sub_sector_format,
):
    """Формат SubSector."""
    url = reverse('api:personal-cabinet:sub-sectors-detail', [sub_sector.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        sub_sector_format(sub_sector)
    )


@pytest.mark.django_db()
def test_sub_sector_list(
    api_client,
):
    """Список SubSector."""
    url = reverse('api:personal-cabinet:sub-sectors-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
