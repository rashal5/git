# Generated by Django 4.2.7 on 2024-01-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_fillfrom_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillfrom',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.department'),
        ),
    ]
