# Create your views here.

from blog.models import Blog, Category, Video
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:4]
    })


def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })


def feed(request):
    return render_to_response('feed.html', {
        'vids': Video.objects.all()[:4]
    })