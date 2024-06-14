import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_problem_subcategory_format(
    api_client,
    problem_subcategory,
    problem_subcategory_format,
):
    """Формат ProblemSubcategory."""
    url = reverse('support:problem-subcategory-detail', [problem_subcategory.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == problem_subcategory_format(problem_subcategory)


@pytest.mark.django_db()
def test_problem_subcategory_post(
    api_client,
):
    """Создание ProblemSubcategory."""
    url = reverse('support:problem-subcategory-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_problem_subcategory_delete(api_client, problem_subcategory):
    """Удаление ProblemSubcategory."""
    url = reverse('support:problem-subcategory-detail', [problem_subcategory.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_problem_subcategory_change(
    api_client,
    problem_subcategory,
):
    """Изменение ProblemSubcategory."""
    url = reverse('api:support:problem-subcategory-detail', [problem_subcategory.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
