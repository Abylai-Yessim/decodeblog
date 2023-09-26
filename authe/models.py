from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

# def uniq_name_upload(instance, filename):
#     new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
#     return f'avatar/{new_file_name}'

# class avatar(models.Model):
#     image =  models.ImageField(blank=True, upload_to=uniq_name_upload)
