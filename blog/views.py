from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'blog/index.html')


def contact(request):
    return render(request, 'blog/contact.html')


def category(request):
    return render(request, 'blog/category.html')


def post(request):
    return render(request, 'blog/post.html')

    



