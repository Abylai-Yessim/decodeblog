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
    path('commentadd/<int:blog_id>/',views.AddComment.as_view(), name='comments-add'),    # Возможно удалить #
    path('testcommentview/<int:blog_id>/', views.BlogDetail.as_view(), name='comments-category'),
    path('search/', views.Search.as_view(), name='search'),

    path('', include(router.urls)),
]