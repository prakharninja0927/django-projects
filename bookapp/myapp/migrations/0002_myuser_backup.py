# Generated by Django 3.2.3 on 2021-05-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='backup',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
