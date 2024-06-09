from datetime import timedelta

import openai
from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import now

from server.apps.investment_object.models import InvestmentObject
from server.apps.personal_cabinet.models import Subscription
from server.apps.personal_cabinet.services.create_business import (
    update_or_create_business,
)
from server.apps.service_interaction.models.event import Event
from server.apps.service_interaction.models.post import Post
from server.apps.services.enums import SubscriptionType, UploadDataFromFileType
from server.apps.services.parsing.xlsx.real_estate import parsing_real_estate
from server.apps.services.parsing.xlsx.specialized_site import \
    parsing_specialized_site
from server.apps.support.models import ServiceSupport
from server.celery import app


@app.task(bind=True)
def delayed_parsing_data(self, file, object_type) -> None:
    """
    Парсинг данных
    """
    if object_type == UploadDataFromFileType.SPECIALIZED_SITE:
        parsing_specialized_site(file)
    if object_type == UploadDataFromFileType.REAL_ESTATE:
        parsing_real_estate(file)
