from django.shortcuts import render

from .models import Post


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts,
        'slug': 'slug',
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
        'slug': slug
    }
    return render(request, template, context)
