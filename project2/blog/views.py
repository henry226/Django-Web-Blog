from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Henry',
        'title': 'Blog Post 1',
        'content': 'Fist post content',
        'date_posted': '8/27, 2018'
    },
    {
        'author': 'Henry',
        'title': 'Blog Post 1',
        'content': 'Fist post content',
        'date_posted': '8/27, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
