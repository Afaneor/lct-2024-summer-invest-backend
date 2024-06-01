# from django.conf import settings
# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class ExtraData(AbstractBaseModel):
#     """Дополнительная информация."""
#
#     investment_site = models.OneToOneField(
#         to='investment_site.InvestmentSite',
#         verbose_name=_('Инвестиционная площадка'),
#         on_delete=models.CASCADE,
#         related_name='extra_datas'
#     )
#     general_info = models.TextField(
#         verbose_name=_('Общая информация'),
#         blank=True,
#     )
#     address = models.CharField(
#         verbose_name=_('Адрес'),
#         blank=True,
#     )
#     area = models.FloatField(
#         verbose_name=_('Общая площадь, м2, га'),
#         blank=True,
#     )
#     ground_area = models.FloatField(
#         verbose_name=_('Общая площадь, га'),
#         blank=True,
#     )
#     investment_size = models.CharField(
#         verbose_name=_('Объем инвестиций, млрд руб'),
#         blank=True,
#     )
#     okrug = models.CharField(
#         verbose_name=_('Округ'),
#         blank=True,
#     )
#     residents_count = models.PositiveSmallIntegerField(
#         verbose_name=_('Количество резидентов ОЭЗ'),
#         blank=True,
#     )
#     workplaces_count = models.PositiveSmallIntegerField(
#         verbose_name=_('Количество рабочих мест'),
#         blank=True,
#     )
#     details_url = models.CharField(
#         verbose_name=_('Адрес объекта на сайте investmoscow.ru'),
#         blank=True,
#     )
#     district_id = models.IntegerField(
#         verbose_name=_('Id района'),
#         blank=True,
#     )
#     district_name = models.IntegerField(
#         verbose_name=_('Название района'),
#         blank=True,
#     )
#     region_id = models.CharField(
#         verbose_name=_('Id региона'),
#         max_length=settings.MAX_STRING_LENGTH,
#     )
#     region_name = models.CharField(
#         verbose_name=_('Название региона'),
#         max_length=settings.MAX_STRING_LENGTH,
#         blank=True,
#     )
#     subway_stations = models.ManyToManyField(
#         'investment_site.SubwayStation',
#         verbose_name=_('предупредительные меры'),
#         blank=True,
#         related_name='funding_plans',
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Дополнительная информация')
#         verbose_name_plural = _('Дополнительная информация')
#
#     def __str__(self):
#         return str(self.investment_site)
