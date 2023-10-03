from django.contrib.auth.models import User
import uuid
from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'avatars/{new_file_name}'

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)


    def __str__(self):
        return self.user.username




# class User(AbstractUser):
#     image = models.ImageField(upload_to='avatars', blank=True)
#     description = models.TextField(max_length=200)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='users',
#         blank=True,
#         verbose_name='groups',
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='users',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Specific permissions for this user.',
#         error_messages={
#             'add': 'The permission you are trying to add already exists for the user.',
#             'remove': 'The permission you are trying to remove does not exist for the user.',
#         },
#     )