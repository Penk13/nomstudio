# Generated by Django 4.2.2 on 2023-06-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_work_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='work',
            name='description',
        ),
    ]
