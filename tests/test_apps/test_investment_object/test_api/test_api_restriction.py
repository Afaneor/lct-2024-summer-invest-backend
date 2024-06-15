import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_restriction_detail(
    api_client,
    restriction,
    restriction_format,
):
    """Формат Restriction."""
    url = reverse('api:investment-object:restrictions-detail', [restriction.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        restriction_format(restriction)
    )


@pytest.mark.django_db()
def test_restriction_list(
    api_client,
):
    """Список Restriction."""
    url = reverse('api:investment-object:restrictions-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
