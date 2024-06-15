import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_apps.conftest import object_without_keys

fake = Faker()


@pytest.mark.django_db()
def test_transaction_form_format(
    api_client,
    transaction_form,
    transaction_form_format,
):
    """Формат TransactionForm."""
    url = reverse(
        'investment-object:transaction-forms-detail',
        [transaction_form.id,
         ])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert (
        object_without_keys(response.json()) ==
        transaction_form_format(transaction_form)
    )


@pytest.mark.django_db()
def test_transaction_form_post(
    api_client,
):
    """Список TransactionForm."""
    url = reverse('api:investment-object:transaction-forms-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
