from django.shortcuts import render
from .models import Page, Post, Song


def home(request):
    return render(request, 'myapp/home.html')


def show_page_data(request):
    page = Page.objects.all()
    return render(request, 'myapp/page.html', {'pages': page})


def show_post_data(request):
    post = Post.objects.all()
    return render(request, 'myapp/post.html', {'posts': post})


def show_song_data(request):
    song = Song.objects.all()
    return render(request, 'myapp/song.html', {'songs': song})
