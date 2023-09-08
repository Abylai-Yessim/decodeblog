from django.shortcuts import render

# Create your views here.



menu = [
    {'title': 'Decode Blog', 'url': 'decode_blog:home'},
]

def home(request):
    data = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'decode_blog/home.html', context=data)

def blog(request):
    data = {
        'menu': menu,
        'title': 'Мои блоги'
    }
    return render(request, 'decode_blog/blog.html', context=data)

def comment(request):
    data = {
        'menu': menu,
        'title': 'Комментарий'
    }
    return render(request, 'decode_blog/comment.html', context=data)

def comment_details(request):
    data = {
        'menu': menu,
        'title': 'Оставить Комментраий'
    }
    return render(request, 'decode_blog/comment_details.html', context=data)

def newblog(request):
    data = {
        'menu': menu,
        'title': 'Новый блог'
    }
    return render(request, 'decode_blog/newblog.html', context=data)