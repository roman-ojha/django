from django.shortcuts import render, HttpResponse
from blog import signals


def home(request):
    # sending signal
    signals.notification.send(
        sender=request.user, request=request, user=['Roman', 'Razz'])
    # we are providing the argument that we define while creating signals
    return HttpResponse('From home page')
