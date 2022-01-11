from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # render takes three argument one is 'request' and another is the html file in this case index.html and third it take dictionary which dictionary can be able to access by the index.html


def analyze(request):
    djtext = request.POST.get('text', 'default')
    # Checking checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charectorcounter = request.POST.get('charectorcounter', 'off')
    # For Remove Punchuations
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        # here we are trying to remove punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': "Remove Punctuations",
            'analyze_text': analyzed
        }
        return render(request, 'analyze.html', params)
    # for UpperCase
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {
            'purpose': "Change to Uppercase",
            'analyze_text': analyzed
        }
        return render(request, 'analyze.html', params)
    # For remove newline
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {
            'purpose': "Remove new line",
            'analyze_text': analyzed
        }
        return render(request, 'analyze.html', params)
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed+char
        params = {
            'purpose': "Remove new line",
            'analyze_text': analyzed
        }
        return render(request, 'analyze.html', params)
    if (charectorcounter == 'on'):
        charcount = 0
        for char in djtext:
            charcount = charcount+1
        params = {
            'purpose': "Charector counter",
            'analyze_text': charcount
        }
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
