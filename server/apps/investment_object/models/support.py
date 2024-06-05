from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel


class Support(AbstractBaseModel):
    """Поддержка."""

    region = models.CharField(
        verbose_name=_('Регион'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
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
    legal_act = models.CharField(
        verbose_name=_('Реквизиты НПА'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    url_legal_act = models.CharField(
        verbose_name=_('Ссылка на НПА'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    application_form_link = models.CharField(
        verbose_name=_('Ссылка на форму подачи заявки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    name_responsible_body = models.CharField(
        verbose_name=_('Наименование ответственного органа власти, администрирующего данную меру поддержки'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    economic_activity = models.ManyToManyField(
        to='investment_object.EconomicActivity',
        verbose_name=_('Экономическая активность'),
        related_name='real_estate'
    )
    restrictions = models.ManyToManyField(
        to='investment_object.Restriction',
        verbose_name=_('Ограничения по видам деятельности'),
        related_name='investment_sites'
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
        verbose_name = _('Поддержка')
        verbose_name_plural = _('Поддержки')

    def __str__(self):
        return str(self.tender)
