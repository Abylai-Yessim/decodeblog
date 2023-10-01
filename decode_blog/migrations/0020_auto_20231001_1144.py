# Generated by Django 3.2.20 on 2023-10-01 05:44

import datetime
import decode_blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decode_blog', '0019_auto_20231001_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to=decode_blog.models.uniq_name_upload)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 10, 1, 11, 44, 27, 985745))),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decode_blog.category')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 11, 44, 27, 985745)),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 11, 44, 27, 985745)),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]