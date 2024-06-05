import openai
from django.conf import settings

from server.apps.personal_cabinet.services.create_business import (
    create_or_update_business,
)
from server.celery import app


@app.task(bind=True)
def delayed_create_business(self, inn: str, user_id: int) -> None:
    """Выбираем нужную информацию о компании или ИП и сохраняем ее в БД.

    Информация берется из DaData.
    """
    create_or_update_business(
        inn=inn,
        user_id=user_id,
    )


# @app.task(bind=True)
# def send_info_in_chat_gpt(self, sector: str, report_id: int) -> None:
#     openai.api_key = settings.OPENAI_API_KEY
#
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=[
#             {
#                 'role': 'user',
#                 'content': 'test'
#             },
#         ],
#         temperature=0.7,
#         top_p=1.0,
#         n=1,
#         max_tokens=2048,
#     )
#     answers = response.choices[0].message.content


