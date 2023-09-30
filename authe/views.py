from typing import Set
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from .forms import *
import sys
sys.path.append("..")
from decode_blog.models import NewBlog

# Create your views here.

menu = [
    {'title': 'Decode blog', 'url': 'decode_blog:Home'},
]

class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'authe/signup.html'
    success_url = reverse_lazy('authe:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('authe:profile')
    

class SignInUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authe/signin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Вход'
        context['menu'] = menu

        return context
    
    def get_success_url(self):
        return reverse_lazy('authe:profile')
    

    
def signout_user(request):
    logout(request)
    return redirect('decode_blog:home')



def profile(request):
    if not request.user.is_authenticated:
        return redirect('authe:signin')
    
    data = {
        'title': 'Профиль',
        'menu': menu,
        'posts': NewBlog.objects.filter(author_id=request.user.id)
    }

    return render(request, 'authe/profile.html', context=data)    


