import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_territorial_location_detail(
    api_client,
    territorial_location,
    territorial_location_format,
):
    """Формат TerritorialLocation."""
    url = reverse(
        'api:personal-cabinet:territorial-locations-detail',
        [territorial_location.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        territorial_location_format(territorial_location)
    )


@pytest.mark.django_db()
def test_territorial_location_list(
    api_client,
):
    """Список TerritorialLocation."""
    url = reverse('api:personal-cabinet:territorial-locations-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
