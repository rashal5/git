# Generated by Django 4.2.7 on 2024-01-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_fillfrom_choice_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillfrom',
            name='filled',
            field=models.BooleanField(default=False),
        ),
    ]
