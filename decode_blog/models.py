from django.db import models
import uuid
import datetime
from django.contrib.auth.models import User


def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'img/{new_file_name}'

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 
    
class NewBlog(models.Model):
    name = models.CharField(max_length=100, null=False, default="")
    image = models.ImageField(blank=True, upload_to=uniq_name_upload)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.today())

    class Meta:
        verbose_name = 'Newlog'
        verbose_name_plural = 'NewBlogs'

    def __str__(self):
        return self.name


class EditBlogModel(models.Model):
    name = models.CharField(max_length=100,)
    image = models.ImageField(blank=True, upload_to=uniq_name_upload)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=False)
    date = models.DateTimeField(default=datetime.datetime.today())

    class Meta:
        verbose_name = 'Editlog'
        verbose_name_plural = 'EditBlogs'

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    date = models.DateTimeField(default=datetime.datetime.today())
    blog = models.ForeignKey(NewBlog, on_delete=models.CASCADE, default=1)
