# Generated by Django 3.2.20 on 2023-09-29 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0017_auto_20230929_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 10, 28, 9, 147247)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 10, 28, 9, 147247)),
        ),
    ]
