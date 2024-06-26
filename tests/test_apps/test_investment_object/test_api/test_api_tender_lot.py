import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys


@pytest.mark.django_db()
def test_tender_lot_detail(
    api_client,
    tender_lot,
    tender_lot_format,
):
    """Формат TenderLot."""
    url = reverse('api:investment-object:tender-lots-detail', [tender_lot.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        tender_lot_format(tender_lot)
    )


@pytest.mark.django_db()
def test_tender_lot_list(
    api_client,
):
    """Список TenderLot."""
    url = reverse('api:investment-object:tender-lots-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
