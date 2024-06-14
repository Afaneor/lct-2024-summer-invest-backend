import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_problem_format(
    api_client,
    problem,
    problem_format,
):
    """Формат Problem."""
    url = reverse('support:problem-detail', [problem.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == problem_format(problem)


@pytest.mark.django_db()
def test_problem_post(
    api_client,
):
    """Создание Problem."""
    url = reverse('support:problem-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_problem_delete(api_client, problem):
    """Удаление Problem."""
    url = reverse('support:problem-detail', [problem.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_problem_change(
    api_client,
    problem,
):
    """Изменение Problem."""
    url = reverse('api:support:problem-detail', [problem.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
