# Generated by Django 4.2.7 on 2024-01-01 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_fillfrom_delete_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillfrom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
