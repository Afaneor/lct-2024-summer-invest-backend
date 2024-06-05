from server.apps.personal_cabinet.tasks import delayed_create_business
from server.apps.user.models import User


def create_new_user(data: dict) -> User:
    """Создание нового пользователя."""
    user = User.objects.create(
        username=data.get('email').split('@')[0],
        email=data.get('email'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        middle_name=data.get('middle_name', ''),
    )

    # Устанавливаем пароль.
    user.set_password(data.get('password1'))
    user.save()
    user.refresh_from_db()

    delayed_create_business.apply_async(
        kwargs={
            'inn': data.get('inn'),
            'user_id': user.id,
        },
    )
    return user
