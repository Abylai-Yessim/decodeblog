from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views 

router = SimpleRouter()
router.register(r'', views.BlogViewSet, basename='blog')

app_name = 'decode_blog'

urlpatterns = [
    path('', views.home, name='home'),
    # path('comment/', views.comment, name='comment'),
    # path('comment_details/', views.comment_details, name='comment_details'),
    path('newblog/', views.DecodeAddBlog.as_view(), name='newblog'),
    path('cmadd/', views.AddComment.as_view(), name='cmadd'),
    path('commentview/<int:blog_id>/', views.BlogDetail.as_view(), name='comments-blog'),
    path('search/', views.search_action, name='search_action'),
    path('search_h/', views.search_h, name='search_h'),
    path('', include(router.urls)),
]