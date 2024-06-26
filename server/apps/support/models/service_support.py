from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services.base_model import AbstractBaseModel
from server.apps.services.content_type_id import get_content_type_id
from server.apps.services.enums import ServiceSupportType


class ServiceSupport(AbstractBaseModel):
    """Сервис поддержки."""

    external_id = models.CharField(
        verbose_name=_('Id объекта'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    region = models.CharField(
        verbose_name=_('Регион'),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    service_support_type = models.CharField(
        verbose_name=_('Тип сервиса'),
        max_length=settings.MAX_STRING_LENGTH,
        choices=ServiceSupportType.choices,
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
        verbose_name=_(
            'Наименование ответственного органа власти, '
            'администрирующего данную меру поддержки',
        ),
        max_length=settings.MAX_STRING_LENGTH,
        blank=True,
    )
    economic_activities = models.ManyToManyField(
        to='investment_object.EconomicActivity',
        verbose_name=_('Экономическая деятельность'),
        related_name='supports',
        blank=True,
    )
    restrictions = models.ManyToManyField(
        to='investment_object.Restriction',
        verbose_name=_('Ограничения по видам деятельности'),
        related_name='supports',
        blank=True,
    )
    msp_roster = models.CharField(
        verbose_name=_('Требуется вхождение в реестр МСП'),
        max_length=settings.MAX_STRING_LENGTH,
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
    url = models.CharField(
        verbose_name=_('Ссылка на объект'),
        blank=True,
    )

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Сервис поддержки')
        verbose_name_plural = _('Сервисы поддержки')
        constraints = [
            models.CheckConstraint(
                name='service_support_type_valid',
                check=models.Q(
                    service_support_type__in=ServiceSupportType.values,
                ),
            ),
        ]

    def __str__(self):
        return self.name

    @property
    def content_type_id(self) -> int:
        """Content type id утечки."""
        return get_content_type_id(self)
