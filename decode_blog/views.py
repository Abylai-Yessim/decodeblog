from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from rest_framework.views import APIView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
# from .models import Newblog 
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from .serializer import *
from django.db.models import Q

# Create your views here.

menu = [
    {'title': 'Decode Blog', 'url': 'decode_blog:home'},
]

#  Переделанное
def search_action(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = NewBlog.objects.filter(Q(name__icontains=search_post) | Q(description__icontains=search_post)) 
    else:
        posts = NewBlog.objects.all()

    return render(request, "authe/profile.html", {
        'posts': posts,
        'menu': menu,
    })
    

def search_h(request):
    search_p = request.GET.get('search_h')
    if search_p:
        pos = NewBlog.objects.filter(Q(name__icontains=search_p) | Q(description__icontains=search_p)) 
    else:
        pos = NewBlog.objects.all()

    return render(request, 'decode_blog/home.html', {
        'newblogs': pos,
    })
    
def home(request):
    newblogs = NewBlog.objects.all()
    categories = Category.objects.all()  

    data = {
        'menu': menu,
        'title': 'Главная страница',
        'newblogs': newblogs,
        'categories': categories,  
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

class EditBlog(UpdateView):
    model = NewBlog
    form_class = AddBlogForm
    template_name = 'decode_blog/edit_blog.html'  
    success_url = reverse_lazy('decode_blog:home')

    def get_object(self):
        blog_id = self.kwargs['blog_id']
        return NewBlog.objects.get(pk=blog_id)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def delete_blog(request, blog_id):
    try:
        blog = get_object_or_404(NewBlog, pk=blog_id)
        blog.delete()
        return redirect('decode_blog:home')  
    except NewBlog.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Blog not found'})




class BlogDetail(DetailView):
    model = NewBlog
    template_name = 'decode_blog/comment.html'
    pk_url_kwarg = 'blog_id'
    context_object_name = 'newblog'
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
    
class CategoriesBlog(ListView):
    model = NewBlog
    template_name = 'decode_blog/home.html'
    context_object_name = 'categories'
    

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        
        # Передача контекстных данных  #
        context['title'] = 'Категории'
        context['menu'] = menu
        context['categories'] = Category.objects.all()

        return context
    
def site_category(request, category_id):
    newblogs = NewBlog.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    data = {
        'newblogs': newblogs,
        'categories':categories,
        'menu':menu,
        'title':'Статьи',
        'category_id':category_id
    }

    return render(request, 'decode_blog/home.html', context=data) 

# class ShowComment(DetailView):
#     model = Comment  # Изменено на модель Comment, чтобы отображать комментарии
#     template_name = 'decode_blog/comment.html'
#     pk_url_kwarg = 'comment_id'


#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if not self.request.user.is_authenticated:
#             return queryset.none()
#         return queryset.filter(blog_id=self.blog_id)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Обзор комментариев'
#         context['blog'] = NewBlog.objects.get(id=self.blog_id)
#         context['menu'] = menu
#         return context






# class CategoriesBlog(ListView):
#     model = NewBlog
#     template_name = 'decode_blog/home.html'
#     context_object_name = 'categories'
    

#     def get_context_data(self, **kwargs):        
#         context = super().get_context_data(**kwargs)
        
        
#         context['title'] = 'Категории'
#         context['menu'] = menu
#         context['categories'] = Category.objects.all()

#         return context
    
# def site_category(request, category_id):
#     blogs = NewBlog.objects.filter(category_id=category_id)
#     categories = Category.objects.all()

#     data = {
#         'blogs':blogs,
#         'categories':categories,
#         'menu':menu,
#         'title':'Статьи',
#         'category_id':category_id
#     }

#     return render(request, 'decode_blog/home.html', context=data) 

class CreateComment(APIView):
    def post(self, request):
        message_text = request.data['comment-text']
        blog_id = request.data['blog_id']
        newblog = NewBlog.objects.get(id=blog_id)
        user = User.objects.get(id=request.user.id)
        new_comment = Comment.objects.create(text=message_text, blog=newblog, user=user)
        new_comment.save()

        return redirect('decode_blog:comments-blog', blog_id)
