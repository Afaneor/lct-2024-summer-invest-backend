import xlrd
from django.core.management.base import BaseCommand

from server.apps.hincal.models import (
    Business,
    BusinessIndicator,
    Sector,
    SubSector,
)


class Command(BaseCommand):
    """Добавление данных в BusinessIndicator"""

    help = 'Добавление данных в BusinessIndicator'

    def handle(self, *args, **options):  # noqa: WPS110
        """Добавление данных в BusinessIndicator"""
        workbook = xlrd.open_workbook('server/apps/hincal/management/commands/data.xls')
        worksheet = workbook.sheet_by_index(0)
        # Iterate the rows and columns
        business_indicator = []
        for i in range(1, 3529):
            if worksheet.cell_value(i, 1) == 'Сведения отсутствуют':
                name_for_sub_sector = 'Иные отрасли'
            else:
                name_for_sub_sector = worksheet.cell_value(i, 1)

            business = Business.objects.create(
                sector=Sector.objects.get(name=worksheet.cell_value(i, 0)),
                sub_sector=SubSector.objects.get(name=name_for_sub_sector),
            )
            business_indicator.append(
                BusinessIndicator(
                    business=business,
                    year=2021,
                    average_number_of_staff=float(worksheet.cell_value(i, 3)),
                    average_salary_of_staff=float(worksheet.cell_value(i, 5)),
                    taxes_to_the_budget=float(worksheet.cell_value(i, 7)),
                    income_tax=float(worksheet.cell_value(i, 9)),
                    property_tax=float(worksheet.cell_value(i, 11)),
                    land_tax=float(worksheet.cell_value(i, 13)),
                    personal_income_tax=float(worksheet.cell_value(i, 15)),
                    transport_tax=float(worksheet.cell_value(i, 17)),
                    other_taxes=float(worksheet.cell_value(i, 19)),
                ),
            )
            business_indicator.append(
                BusinessIndicator(
                    business=business,
                    year=2022,
                    average_number_of_staff=float(worksheet.cell_value(i, 2)),
                    average_salary_of_staff=float(worksheet.cell_value(i, 4)),
                    taxes_to_the_budget=float(worksheet.cell_value(i, 6)),
                    income_tax=float(worksheet.cell_value(i, 8)),
                    property_tax=float(worksheet.cell_value(i, 10)),
                    land_tax=float(worksheet.cell_value(i, 12)),
                    personal_income_tax=float(worksheet.cell_value(i, 14)),
                    transport_tax=float(worksheet.cell_value(i, 16)),
                    other_taxes=float(worksheet.cell_value(i, 18)),
                ),
            )
            print(f'Обработана строка № {i}')
        BusinessIndicator.objects.bulk_create(business_indicator)
