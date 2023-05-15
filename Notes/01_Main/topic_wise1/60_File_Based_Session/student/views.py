from django.shortcuts import render
from datetime import datetime, timedelta


def setSession(request):
    request.session['name'] = 'Roman'
    request.session['lname'] = 'Ojha'
    return render(request, 'student/setsession.html')


def getSession(request):
    name = request.session['name']
    name = request.session.get('name')
    name = request.session.get('name', default="Guest")
    lname = request.session.get('lname', default="Guest")
    return render(request, 'student/getsession.html', {'name': name, 'lname': lname})


def deleteSession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')
