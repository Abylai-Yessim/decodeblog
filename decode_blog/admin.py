from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(NewBlog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'author', 'image', 'date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','text', 'date', 'blog_id')
   
