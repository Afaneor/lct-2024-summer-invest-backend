from django.db import models

from server.apps.hincal.models import Business, Report
from server.apps.user.models import User


def get_all_statistics():
    """Получить общую статистику по системе."""
    business = Business.objects.all()
    reports = Report.objects.all().aggregate(
        average_investment_amount_bi=models.Avg('total_investment_amount_bi'),
        average_investment_amount_math=models.Avg(
            'total_investment_amount_math'),
        total_investment_amount_bi=models.Sum('total_investment_amount_bi'),
        total_investment_amount_math=models.Sum('total_investment_amount_math'),
        number_of_reports=models.Count('pk'),
    )
    popular_reports = Report.objects.values(
        sector_name=models.F('sector__name'),
    ).annotate(
        count=models.Count('pk'),
    )
    return {
        'popular_sector': list(popular_reports),
        'average_investment_amount_bi': reports.get(
            'average_investment_amount_bi',
        ),
        'average_investment_amount_math': reports.get(
            'average_investment_amount_math',
        ),
        'total_investment_amount_bi': reports.get('total_investment_amount_bi'),
        'total_investment_amount_math': reports.get(
            'total_investment_amount_math',
        ),
        'number_of_reports': reports.get('number_of_reports'),
        'number_of_business': business.count(),
    }


def get_user_statistics(user: User):
    """Получить статистику по пользователю."""
    reports = Report.objects.filter(user=user).aggregate(
        average_investment_amount_bi=models.Avg('total_investment_amount_bi'),
        average_investment_amount_math=models.Avg(
            'total_investment_amount_math',
        ),
        total_investment_amount_bi=models.Sum('total_investment_amount_bi'),
        total_investment_amount_math=models.Sum('total_investment_amount_math'),
        number_of_reports=models.Count('pk'),
    )
    popular_reports = Report.objects.values(
        sector_name=models.F('sector__name'),
    ).annotate(
        count=models.Count('pk'),
    )
    return {
        'popular_sector': list(popular_reports),
        'average_investment_amount_bi': reports.get(
            'average_investment_amount_bi',
        ),
        'average_investment_amount_math': reports.get(
            'average_investment_amount_math',
        ),
        'total_investment_amount_bi': reports.get('total_investment_amount_bi'),
        'total_investment_amount_math': reports.get(
            'total_investment_amount_math',
        ),
        'number_of_reports': reports.get('number_of_reports'),
    }
