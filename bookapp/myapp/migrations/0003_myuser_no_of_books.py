# Generated by Django 3.2.3 on 2021-05-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_myuser_backup'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='no_of_books',
            field=models.IntegerField(default=0),
        ),
    ]
