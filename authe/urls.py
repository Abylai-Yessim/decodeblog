from django.urls import path
from . import views 

app_name = 'authe'

urlpatterns = [
    path('signup/', views.SignUpUser.as_view(), name='signup'),
]