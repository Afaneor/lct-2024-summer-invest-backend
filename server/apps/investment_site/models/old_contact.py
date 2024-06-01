# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class Contact(AbstractBaseModel):
#     """Контакт."""
#
#     investment_site = models.OneToOneField(
#         to='investment_site.InvestmentSite',
#         verbose_name=_('Инвестиционная площадка'),
#         on_delete=models.CASCADE,
#         related_name='contacts'
#     )
#     address = models.CharField(
#         verbose_name=_('Адрес'),
#     )
#     contact_person = models.CharField(
#         verbose_name=_('Контактное лицо'),
#     )
#     management_company = models.CharField(
#         verbose_name=_('Управляющая компания'),
#     )
#     phone = models.CharField(
#         verbose_name=_('Телефон'),
#     )
#     url = models.CharField(
#         verbose_name=_('Url сайта'),
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Контакт')
#         verbose_name_plural = _('Контакты')
#
#     def __str__(self):
#         return str(self.investment_site)
