# Generated by Django 3.2.3 on 2021-05-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_bookcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
