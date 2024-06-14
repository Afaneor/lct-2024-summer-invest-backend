import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_specialized_site_format(
    api_client,
    specialized_site,
    specialized_site_format,
):
    """Формат SpecializedSite."""
    url = reverse('investment-object:specialized-site-detail', [specialized_site.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == specialized_site_format(specialized_site)


@pytest.mark.django_db()
def test_specialized_site_post(
    api_client,
):
    """Создание SpecializedSite."""
    url = reverse('investment-object:specialized-site-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_specialized_site_delete(api_client, specialized_site):
    """Удаление SpecializedSite."""
    url = reverse('investment-object:specialized-site-detail', [specialized_site.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_specialized_site_change(
    api_client,
    specialized_site,
):
    """Изменение SpecializedSite."""
    url = reverse('api:investment-object:specialized-site-detail', [specialized_site.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
