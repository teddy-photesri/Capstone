from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post


def home(request):
    context = {
        'posts': Post.object.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
