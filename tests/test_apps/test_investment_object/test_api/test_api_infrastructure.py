import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_infrastructure_format(
    api_client,
    infrastructure,
    infrastructure_format,
):
    """Формат Infrastructure."""
    url = reverse(
        'api:investment-object:infrastructures-detail',
        [infrastructure.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        infrastructure_format(infrastructure)
    )


@pytest.mark.django_db()
def test_infrastructure_list(
    api_client,
):
    """Список Infrastructure."""
    url = reverse('api:investment-object:infrastructures-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
