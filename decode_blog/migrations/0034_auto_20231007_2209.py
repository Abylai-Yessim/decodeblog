# Generated by Django 3.2.20 on 2023-10-07 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0033_auto_20231003_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 7, 22, 9, 32, 927986)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 7, 22, 9, 32, 926988)),
        ),
    ]
