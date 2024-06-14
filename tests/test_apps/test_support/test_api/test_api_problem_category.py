import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_problem_category_format(
    api_client,
    problem_category,
    problem_category_format,
):
    """Формат ProblemCategory."""
    url = reverse('support:problem-category-detail', [problem_category.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == problem_category_format(problem_category)


@pytest.mark.django_db()
def test_problem_category_post(
    api_client,
):
    """Создание ProblemCategory."""
    url = reverse('support:problem-category-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_problem_category_delete(api_client, problem_category):
    """Удаление ProblemCategory."""
    url = reverse('support:problem-category-detail', [problem_category.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_problem_category_change(
    api_client,
    problem_category,
):
    """Изменение ProblemCategory."""
    url = reverse('api:support:problem-category-detail', [problem_category.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
