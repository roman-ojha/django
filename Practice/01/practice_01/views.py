from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {
        "name": "roman",
        "place": "earth",
    }
    return render(request, 'index.html', params)


def about(request):
    name = "Roman"
    return HttpResponse(f"<h1>This is the about page {name}</h1>")


def getData(request):
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    gender = "none"
    if(request.GET.get('male', 'off') == "on"):
        gender = "male"
    elif(request.GET.get('female', 'off') == "on"):
        gender = "female"
    elif(request.GET.get('others', 'off') == "on"):
        gender = "Others"
    else:
        pass
    params = {
        "name": name,
        "email": email,
        "gender": gender,
    }
    return render(request, 'userData.html', params)
