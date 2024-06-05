import openai
from django.conf import settings

from server.apps.personal_cabinet.models.message import Message
from server.apps.personal_cabinet.services.enums import MessageOwnerType


def send_data_in_chat_gpt(
    user_text: str,
    selection_request_id: int,
    message_id: int,
) -> None:
    """
    Отправляем информацию в ChatGpt.
    """
    openai.api_key = settings.OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': user_text,
            },
        ],
        temperature=0.7,
        top_p=1.0,
        n=1,
        max_tokens=2048,
    )
    answers = response.choices[0].message.content

    Message.objects.create(
        owner_type=MessageOwnerType.BOT,
        selection_request_id=selection_request_id,
        text=answers,
        parent_id=message_id,
    )

    # Логика по поиску инвестиционных площадок...

    return answers
