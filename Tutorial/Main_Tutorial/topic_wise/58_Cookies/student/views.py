from django.shortcuts import render
from datetime import datetime, timedelta


def setCookie(request):
    print("hello")
    # we will store the returned response object
    response = render(request, 'student/setcookies.html')
    # now we will set the cookie
    response.set_cookie('name', 'Roman')
    response.set_cookie('name', 'Roman', max_age=60,
                        expires=datetime.utcnow()+timedelta(days=2), path='/')
    # after that we will return the response
    return response


def getCookie(request):
    # we can get the cookies from request object
    # accessing 'name' cookie
    name = request.COOKIES['name']
    name = request.COOKIES.get('name')
    name = request.COOKIES.get('name', 'default_value')
    print(name)
    return render(request, 'student/getcookies.html', {'name': name})


def deleteCookie(request):
    # we can delete cookie using response object
    response = render(request, 'student/delcookies.html')
    response.delete_cookie('name')
    return response


def setSignedCookies(request):
    response = render(request, 'student/setcookies.html')
    # setting signed cookies
    response.set_signed_cookie(
        'name', 'Roman', salt="this is the salt", expires=datetime.utcnow()+timedelta(days=2))
    # required a salt to get the cookie
    return response


def getSignedCookies(request):
    # required a salt to get the cookie
    # if you don't want to get error if 'salt' value didn't match then you can use the default value while getting the cookies
    name = request.get_signed_cookie(
        'name', salt="this is the salt", default="Guest")
    return render(request, 'student/getcookies.html', {'name': name})
