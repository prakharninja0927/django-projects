# Generated by Django 3.2.3 on 2021-05-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_myuser_no_of_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('type', models.CharField(blank=True, max_length=150)),
                ('book_name', models.CharField(blank=True, max_length=150)),
                ('author', models.CharField(blank=True, max_length=150)),
                ('u_name', models.CharField(blank=True, max_length=150)),
                ('date_upload', models.DateTimeField(auto_now=True, verbose_name='upload date')),
                ('no_pages', models.CharField(default='no data', max_length=100)),
            ],
        ),
    ]
