# Generated by Django 4.2.13 on 2024-05-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hincal', '0004_alter_archive_personal_income_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='year',
            field=models.PositiveIntegerField(
                default=2024, verbose_name='Год, к которому относятся данные'
            ),
        ),
    ]
