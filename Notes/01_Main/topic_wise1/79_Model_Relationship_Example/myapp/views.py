from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Page, Post, Song


def home(request):
    return render(request, 'myapp/home.html')


def show_user_data(request):
    users = User.objects.all()
    users = User.objects.filter(page__page_cat='blog')
    # here we are getting all the user whose 'Page' model 'page_cat' is blog
    # User.objects.filter(<model_class_name>__<field_name>='<query_value>')

    # users = User.objects.filter(post__post_publish_date='2020-05-28')

    users = User.objects.filter(mysong__song_duration=32)
    # used 'related_name' field for 'Song' model
    return render(request, 'myapp/user.html', {'users': users})


def show_page_data(request):
    pages = Page.objects.all()
    pages = Page.objects.filter(user__email='roman@gmail.com')
    # getting user show email is 'roman@gmail.com'
    return render(request, 'myapp/page.html', {'pages': pages})


def show_post_data(request):
    post = Post.objects.all()
    return render(request, 'myapp/post.html', {'posts': post})


def show_song_data(request):
    songs = Song.objects.all()
    songs = Song.objects.filter(user__username='roman')
    return render(request, 'myapp/song.html', {'songs': songs})
