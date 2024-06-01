# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class Building(AbstractBaseModel):
#     """Здание."""
#
#     investment_site = models.OneToOneField(
#         to='investment_site.InvestmentSite',
#         verbose_name=_('Инвестиционная площадка'),
#         on_delete=models.CASCADE,
#         related_name='buildings'
#     )
#     area = models.FloatField(
#         verbose_name=_('Площадь'),
#     )
#     count = models.CharField(
#         verbose_name=_('Количество объектов'),
#         default='0',
#     )
#     year = models.CharField(
#         verbose_name=_('Год постройки'),
#         default='Не определен',
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Здание')
#         verbose_name_plural = _('Здания')
#
#     def __str__(self):
#         return str(self.investment_site)
