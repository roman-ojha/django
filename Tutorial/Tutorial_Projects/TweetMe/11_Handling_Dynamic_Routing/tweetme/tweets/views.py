from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW 
    Consume by Javascript of swift or java/IOS/Android
    return json data
    """
    # now here rather than sending just httpresponse we will response json data
    # for that we will use 'JsonResponse'
    data = {
        "id": tweet_id,
        # "image_path":obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        # here we can get the document or object from the database using id
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    # return HttpResponse(f"<h1>Hello {tweet_id}-{obj.content}</h1>")
    return JsonResponse(data, status=status)
    # json.dumps, content_type="application/json"
