from django.contrib import admin
from .models import UserProfile

# для теста
admin.site.register(UserProfile)