# Generated by Django 3.2.20 on 2023-09-26 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0004_auto_20230925_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 12, 24, 57, 26833)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 12, 24, 57, 26833)),
        ),
    ]
