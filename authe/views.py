from typing import Set
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

menu = [
    {'title': 'Home', 'url': 'decode_blog:Home'},
]


class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'authe/signup.html'
    # success_url = reverse_lazy('market:signin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('decode_blog:blog')