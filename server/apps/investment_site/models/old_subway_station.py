# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from server.apps.services.base_model import AbstractBaseModel
#
#
# class SubwayStation(AbstractBaseModel):
#     """Станция метро."""
#
#     subway_station_id = models.IntegerField(
#         verbose_name=_('Id станции метро'),
#     )
#     subway_station_name = models.IntegerField(
#         verbose_name=_('Название станции метро'),
#     )
#
#     class Meta(AbstractBaseModel.Meta):
#         verbose_name = _('Станция метро')
#         verbose_name_plural = _('Станции метро')
#
#     def __str__(self):
#         return self.subway_station_name
