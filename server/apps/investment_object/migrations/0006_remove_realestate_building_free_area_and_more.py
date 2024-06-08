# Generated by Django 5.0.6 on 2024-06-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_object', '0005_alter_investmentobject_transaction_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate', name='building_free_area',
        ),
        migrations.RemoveField(model_name='realestate', name='land_free_area',),
        migrations.RemoveField(model_name='realestate', name='municipality',),
        migrations.RemoveField(model_name='realestate', name='owner_website',),
        migrations.RemoveField(
            model_name='specializedsite', name='total_area',
        ),
        migrations.AddField(
            model_name='investmentobject',
            name='building_area',
            field=models.FloatField(
                null=True, verbose_name='Площадь помещений'
            ),
        ),
        migrations.AddField(
            model_name='investmentobject',
            name='land_area',
            field=models.FloatField(null=True, verbose_name='Площадь земли'),
        ),
    ]
