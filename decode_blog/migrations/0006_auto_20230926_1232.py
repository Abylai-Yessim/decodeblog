# Generated by Django 3.2.20 on 2023-09-26 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0005_auto_20230926_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 12, 32, 35, 507644)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 12, 32, 35, 507644)),
        ),
    ]
