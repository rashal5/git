# Generated by Django 5.0.1 on 2024-01-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_pdfdocument_explain_alter_pdfdocument_link_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Program',
            new_name='Memo',
        ),
    ]
