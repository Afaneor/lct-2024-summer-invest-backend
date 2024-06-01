# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class LandPlot(AbstractBaseModel):
#     """Земельный участок."""
#
#     investment_site = models.OneToOneField(
#         to='investment_site.InvestmentSite',
#         verbose_name=_('Инвестиционная площадка'),
#         on_delete=models.CASCADE,
#         related_name='land_plots'
#     )
#     area = models.FloatField(
#         verbose_name=_('Площадь'),
#     )
#     area_unit = models.CharField(
#         verbose_name=_('Единица изменения площади'),
#     )
#     cadastral_number = models.CharField(
#         verbose_name=_('Кадастровый № ЗУ'),
#     )
#     gpzu_date = models.DateField(
#         verbose_name=_('Дата ГПЗУ'),
#     )
#     gpzu_number = models.CharField(
#         verbose_name=_('Номер ГПЗУ'),
#     )
#     vri = models.CharField(
#         verbose_name=_('ВРИ'),
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Земельный участок')
#         verbose_name_plural = _('Земельные участки')
#
#     def __str__(self):
#         return str(self.investment_site)
