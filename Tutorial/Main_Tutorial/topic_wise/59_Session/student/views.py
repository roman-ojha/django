from django.shortcuts import render
from datetime import datetime, timedelta


def setSession(request):
    # setting session using request object
    request.session['name'] = 'Roman'
    request.session['lname'] = 'Ojha'
    return render(request, 'student/setsession.html')


def getSession(request):
    # getting set session using request object
    name = request.session['name']
    name = request.session.get('name')
    name = request.session.get('name', default="Guest")
    lname = request.session.get('lname', default="Guest")
    return render(request, 'student/getsession.html', {'name': name, 'lname': lname})


def deleteSession(request):
    # first we will check does session exist on given key
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')


def methods(request):
    # we can access these method as variable inside django template
    # keys()
    keys = request.session.keys()
    print("Keys: ", keys)
    return render(request, 'student/setsession.html')
