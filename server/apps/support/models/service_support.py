from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.support.services.enums import TypeServiceSupport


class ServiceSupport(AbstractBaseModel):
    """Сервис поддержки."""

    region = models.CharField(
        verbose_name=_('Регион'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    type_service_support = models.CharField(
        verbose_name=_('Тип сервиса'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=TypeServiceSupport.choices,
    )
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    support_type = models.CharField(
        verbose_name=_('Тип поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    support_level = models.CharField(
        verbose_name=_('Уровень поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        blank=True,
    )
    legal_act = models.TextField(
        verbose_name=_('Реквизиты НПА'),
        blank=True,
    )
    url_legal_act = models.TextField(
        verbose_name=_('Ссылка на НПА'),
        blank=True,
    )
    url_application_form = models.CharField(
        verbose_name=_('Ссылка на форму подачи заявки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    name_responsible_body = models.CharField(
        verbose_name=_('Наименование ответственного органа власти, администрирующего данную меру поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    economic_activities = models.ManyToManyField(
        to='investment_object.EconomicActivity',
        verbose_name=_('Экономическая активность'),
        related_name='supports',
        blank=True,
    )
    restrictions = models.ManyToManyField(
        to='investment_object.Restriction',
        verbose_name=_('Ограничения по видам деятельности'),
        related_name='supports',
        blank=True,
    )
    is_msp_roster = models.BooleanField(
        verbose_name=_('Требуется вхождение в реестр МСП'),
        null=True,
        blank=True,
    )
    applicant_requirement = models.TextField(
        verbose_name=_('Требование к заявителю'),
        blank=True,
    )
    applicant_procedure = models.TextField(
        verbose_name=_('Процедура подачи заявки'),
        blank=True,
    )
    required_document = models.TextField(
        verbose_name=_('Необходимые документы'),
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Сервис поддержки')
        verbose_name_plural = _('Сервисы поддержки')
        constraints = [
            models.CheckConstraint(
                name='type_service_support_valid',
                check=models.Q(type_service_support__in=TypeServiceSupport.values),
            ),
        ]

    def __str__(self):
        return self.name
