# Generated by Django 3.2.20 on 2023-10-01 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0021_auto_20231001_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 12, 4, 59, 534495)),
        ),
        migrations.AlterField(
            model_name='editblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 12, 4, 59, 534495)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 12, 4, 59, 534495)),
        ),
    ]
