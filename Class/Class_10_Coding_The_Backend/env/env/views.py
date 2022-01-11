from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # render takes three argument one is 'request' and another is the html file in this case index.html and third it take dictionary which dictionary can be able to access by the index.html 


def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    analyzed=djtext
    if removepunc == "on":
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        # here we are trying to remove punctuation
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={
            'purpose':"Remove Punctuations",
            'analyze_text':analyzed
        }
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")