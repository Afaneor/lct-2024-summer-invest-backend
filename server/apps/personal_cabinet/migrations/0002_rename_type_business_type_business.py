# Generated by Django 5.0.6 on 2024-06-06 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_cabinet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business', old_name='type', new_name='type_business',
        ),
    ]
