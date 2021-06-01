# Generated by Django 3.2.3 on 2021-05-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_bookcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookcount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=150)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
