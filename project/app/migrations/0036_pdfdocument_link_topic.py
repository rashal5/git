# Generated by Django 5.0.1 on 2024-01-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_remove_video_course_remove_yourmodel_submitter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='link_topic',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]