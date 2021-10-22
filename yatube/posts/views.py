from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Group, User



def index(request):
    posts_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_list = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'page_obj': page_obj
    }

    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)
