# Generated by Django 3.2.20 on 2023-10-02 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0027_auto_20231002_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 19, 24, 47, 464579)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 19, 24, 47, 464579)),
        ),
    ]