# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class EngineeringInfrastructure(AbstractBaseModel):
#     """Инженерная инфраструктура."""
#
#     investment_site = models.OneToOneField(
#         to='investment_site.InvestmentSite',
#         verbose_name=_('Инвестиционная площадка'),
#         on_delete=models.CASCADE,
#         related_name='engineering_infrastructure'
#     )
#     heating_supply_free_power = models.FloatField(
#         verbose_name=_('Теплоснабжение. Свободная мощность'),
#     )
#     heating_supply_max_available_power = models.FloatField(
#         verbose_name=_('Теплоснабжение. Максимально допустимая мощность'),
#     )
#     power_supply_free_power = models.FloatField(
#         verbose_name=_('Электроснабжение. Свободная мощность'),
#     )
#     power_supply_max_available_power = models.FloatField(
#         verbose_name=_('Электроснабжение. Максимально допустимая мощность'),
#     )
#     sewers_free_power = models.FloatField(
#         verbose_name=_('Водоотведение. Свободная мощность'),
#     )
#     sewers_max_available_power = models.FloatField(
#         verbose_name=_('Водоотведение. Максимально допустимая мощность'),
#     )
#     water_supply_free_power = models.FloatField(
#         verbose_name=_('Водоснабжение. Свободная мощность'),
#     )
#     water_supply_max_available_power = models.FloatField(
#         verbose_name=_('Водоснабжение. Максимально допустимая мощность'),
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Инженерная инфраструктура')
#         verbose_name_plural = _('Инженерные инфраструктуры')
#
#     def __str__(self):
#         return str(self.investment_site)
