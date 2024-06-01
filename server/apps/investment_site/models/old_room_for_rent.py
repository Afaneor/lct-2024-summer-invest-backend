# from django.conf import settings
# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class RoomForRent(AbstractBaseModel):
#     """Помещение под аренду."""
#
#     investment_site = models.OneToOneField(
#         to='investment_site.InvestmentSite',
#         verbose_name=_('Инвестиционная площадка'),
#         on_delete=models.CASCADE,
#         related_name='room_for_rents'
#     )
#     area = models.CharField(
#         verbose_name=_('Площадь помещений под аренду'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     electricity = models.CharField(
#         verbose_name=_('Электроэнергия'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     heating = models.CharField(
#         verbose_name=_('Отопление'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     parking = models.CharField(
#         verbose_name=_('Парковка'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     price = models.CharField(
#         verbose_name=_('Стоимость площадки'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     room_type = models.CharField(
#         verbose_name=_('Тип площадки'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     water = models.CharField(
#         verbose_name=_('Вода'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Помещение под аренду')
#         verbose_name_plural = _('Помещения под аренду')
#
#     def __str__(self):
#         return str(self.investment_site)
