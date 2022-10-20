# Generated by Django 4.1.2 on 2022-10-20 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='address',
            field=models.CharField(max_length=177),
        ),
        migrations.AlterField(
            model_name='owner',
            name='passport',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='owning',
            name='begin_date',
            field=models.DateField(default=datetime.date(2018, 1, 1)),
        ),
        migrations.AlterField(
            model_name='owning',
            name='end_date',
            field=models.DateField(default=datetime.date(2020, 1, 1)),
        ),
    ]
