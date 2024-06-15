import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_specialized_site_detail(
    api_client,
    specialized_site,
    specialized_site_format,
):
    """Формат SpecializedSite."""
    url = reverse(
        'api:investment-object:specialized-sites-detail',
        [specialized_site.id],
    )

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        specialized_site_format(specialized_site)
    )


@pytest.mark.django_db()
def test_specialized_site_list(
    api_client,
):
    """Список SpecializedSite."""
    url = reverse('api:investment-object:specialized-sites-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
