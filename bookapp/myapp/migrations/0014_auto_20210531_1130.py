# Generated by Django 3.2.3 on 2021-05-31 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20210531_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='type',
        ),
    ]
