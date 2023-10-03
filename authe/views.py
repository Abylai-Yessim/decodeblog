from typing import Set
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import ProfileEditForm  # Import your profile edit form
# from django.contrib.auth.models import User
from .forms import *
import sys
sys.path.append("..")
from decode_blog.models import NewBlog
from decode_blog.forms import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import *
from .forms import *
from .serializers import *
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
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
    # создание профиля пользователя, если он не существует
        user_profile = UserProfile.objects.create(user=request.user)

    data = {
        'title': 'Профиль',
        'menu': menu,
        'newblogs': NewBlog.objects.filter(author_id=request.user.id),
        # передаем user_profile для аватарки
        'user_profile': user_profile
    }

    return render(request, 'authe/profile.html', context=data)    


class ModelEditBlog(UpdateView):
    model = NewBlog
    form_class = AddBlogForm
    template_name = 'authe/model-edit-blog.html'  
    success_url = reverse_lazy('authe:profile')

    def get_object(self):
        blog_id = self.kwargs['blog_id']
        return NewBlog.objects.get(pk=blog_id)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def model_delete_blog(request, blog_id):
    try:
        blog = get_object_or_404(NewBlog, pk=blog_id)
        blog.delete()
        return redirect('authe:profile')  
    except NewBlog.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Blog not found'})

# ИЗМЕНЕНО
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
    # Создание профиля пользователя, если он не существует
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            new_username = form.cleaned_data['username']

            # проверка username
            if new_username != request.user.username:
                request.user.username = new_username
                request.user.save()

            # проверка фотки
            if 'avatar' in request.FILES:
                user_profile.avatar = request.FILES['avatar']
                user_profile.save()

            # просто bio
            new_bio = form.cleaned_data['bio']
            user_profile.bio = new_bio
            user_profile.save()

            return redirect('authe:profile')
    else:
        form = ProfileEditForm(initial={
            'username': request.user.username,
            'bio': user_profile.bio
        })

    return render(request, 'authe/edit_profile.html', {
        'form': form, 
        'user_profile': user_profile
    })




# class UserDetailAPIView(RetrieveAPIView):
#     def get_queryset(self):
#         return User.objects.get(id=self.request.user.id)
    
# class UserViewSet(GenericViewSet, mixins.CreateModelMixin,):
#     def get_queryset(self):
#         if self.action == 'retrieve':
#             return User.objects.get(id=self.request.user.id)
#         return User.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'create':
#             return UserCreateSerializer
#         elif self.action == 'retrieve':
#             return UserRetrieveSerializer
        
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_queryset()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)