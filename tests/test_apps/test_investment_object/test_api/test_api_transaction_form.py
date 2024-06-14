import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_transaction_form_format(
    api_client,
    transaction_form,
    transaction_form_format,
):
    """Формат TransactionForm."""
    url = reverse('investment-object:transaction-form-detail', [transaction_form.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == transaction_form_format(transaction_form)


@pytest.mark.django_db()
def test_transaction_form_post(
    api_client,
):
    """Создание TransactionForm."""
    url = reverse('investment-object:transaction-form-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_transaction_form_delete(api_client, transaction_form):
    """Удаление TransactionForm."""
    url = reverse('investment-object:transaction-form-detail', [transaction_form.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_transaction_form_change(
    api_client,
    transaction_form,
):
    """Изменение TransactionForm."""
    url = reverse('api:investment-object:transaction-form-detail', [transaction_form.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
