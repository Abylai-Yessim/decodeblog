# Generated by Django 3.2.20 on 2023-10-03 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0032_auto_20231003_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 22, 40, 12, 864782)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 22, 40, 12, 864782)),
        ),
    ]
