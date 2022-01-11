from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    # so in url.py if we will use:
    # path("tweets/<int:tweet_id>", home_view),
    # so here we can see we have to dynamic url at that time use can fill any sort of value inside that <int:tweet_id>
    # then inside the 'kwargs' id we will get : {'tweet_id': 432143}

    # or we can use 'tweet_id' as to get the passing parameter
    return HttpResponse(f"<h1>Hello {tweet_id}</h1>")
