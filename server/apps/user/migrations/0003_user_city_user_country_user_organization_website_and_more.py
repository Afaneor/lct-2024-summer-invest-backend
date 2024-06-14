# Generated by Django 5.0.6 on 2024-06-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_create_super_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(
                blank=True, max_length=255, verbose_name='Город'
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(
                blank=True, max_length=255, verbose_name='Страна'
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='organization_website',
            field=models.URLField(
                blank=True, max_length=255, verbose_name='Сайт организации'
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(
                default='неищвесзвестная должность',
                max_length=255,
                verbose_name='Сайт организации',
            ),
            preserve_default=False,
        ),
    ]
