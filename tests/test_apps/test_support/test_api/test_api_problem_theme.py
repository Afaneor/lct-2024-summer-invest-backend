import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_problem_theme_format(
    api_client,
    problem_theme,
    problem_theme_format,
):
    """Формат ProblemTheme."""
    url = reverse('support:problem-theme-detail', [problem_theme.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response == problem_theme_format(problem_theme)


@pytest.mark.django_db()
def test_problem_theme_post(
    api_client,
):
    """Создание ProblemTheme."""
    url = reverse('support:problem-theme-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_problem_theme_delete(api_client, problem_theme):
    """Удаление ProblemTheme."""
    url = reverse('support:problem-theme-detail', [problem_theme.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_problem_theme_change(
    api_client,
    problem_theme,
):
    """Изменение ProblemTheme."""
    url = reverse('api:support:problem-theme-detail', [problem_theme.id])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
