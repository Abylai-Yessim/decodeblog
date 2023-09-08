from django.urls import path
from . import views 

app_name = 'decode_blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('comment/', views.comment, name='comment'),
    path('comment_details/', views.comment_details, name='comment_details'),
    path('newblog/', views.newblog, name='newblog'),
]