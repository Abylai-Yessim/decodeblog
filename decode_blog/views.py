from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework.viewsets import ModelViewSet
# from .models import Newblog 
from .models import *
from .forms import *
from .serializer import *

# Create your views here.

menu = [
    {'title': 'Decode Blog', 'url': 'decode_blog:home'},
]


class Search(ListView):
    template_name = 'authe/profile.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return NewBlog.objects.filter(name__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
    


def home(request):
    data = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'decode_blog/home.html', context=data)

class DecodeAddBlog(CreateView):
    form_class = AddBlogForm
    template_name = 'decode_blog/newblog.html'
    success_url = reverse_lazy('authe:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Новый продукт'
        context['menu'] = menu

        return context
    
class BlogDetail(DetailView):
    model = NewBlog
    template_name = 'decode_blog/comment.html'
    pk_url_kwarg = 'blog_id'
    context_object_name = 'blog'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обзор блога'
        context['comments'] = Comment.objects.filter(blog_id=self.kwargs['blog_id'])
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context

    
class BlogViewSet(ModelViewSet):
    queryset = NewBlog.objects.all()
    serializer_class = BlogSerializer

    @action(methods=['get'], detail=False)    # ДЛя блогов  #
    def blogs(self, request):
        blogs = NewBlog.objects.all()
        return Response([blog.name for blog in blogs])
            
    @action(methods=['get'], detail=False)
    def genre_filter(self, request):
        categ = NewBlog.objects.filter(categ_id=self.request.query_params.get('categ_id'))   # Для категорий #
        serializer = BlogSerializer(NewBlog, many=True)
        return Response(serializer.data)



def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method "DELETE" not allowed.'})
        
        try:
            instance = NewBlog.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exists.'})
        
        return Response({'status': 'Blog was deleted.'})


class AddComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'decode_blog/Add-comment.html'
    success_url = reverse_lazy('decode_blog:home')     # Переход после создания продукта #
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Привязать комментарий к текущему пользователю #
        blog_id = self.kwargs.get('blog_id')

        if blog_id:                                # Связка комментария с определенным блогом #
            form.instance.blog_id = blog_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новый комментарий'
        context['menu'] = menu

        return context
    


class ShowComment(DetailView):
    model = Comment  # Изменено на модель Comment, чтобы отображать комментарии
    template_name = 'decode_blog/comment.html'
    pk_url_kwarg = 'comment_id'


    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(blog_id=self.blog_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обзор комментариев'
        context['blog'] = NewBlog.objects.get(id=self.blog_id)
        context['menu'] = menu
        return context

