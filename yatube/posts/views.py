from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('index page')


def group_posts(request, slug):
    return HttpResponse('group  page')
