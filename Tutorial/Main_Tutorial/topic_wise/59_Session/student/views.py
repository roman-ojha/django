from django.shortcuts import render
from datetime import datetime, timedelta


def setSession(request):
    # setting session using request object
    request.session['name'] = 'Roman'
    # setting expiry date
    # expire on 5 second
    request.session.set_expiry(5)
    # expire on browser close:
    # request.session.set_expiry(0)

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
    # we can access these session values inside django template

    # keys()
    keys = request.session.keys()
    print("Keys: ", keys)
    # Output: Keys:  dict_keys(['name', 'lname'])

    # items():
    items = request.session.items()
    print("Items: ", items)
    # Output: Items:  dict_items([('name', 'Roman'), ('lname', 'Ojha')]

    # setdefault():
    age = request.session.setdefault('age', '89')
    print("Age: ", age)

    # flush()
    # flush the session and cookie of request user
    # request.session.flush()

    # get session age
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())

    # just by adding expiry date on set will only clear session from the browser too
    # to delete the expired session from database we have to remove the session from database as well
    request.session.clear_expired()

    return render(request, 'student/setsession.html')


# Other methods:
def setTestCookie(request):
    # to set the test cookie to check wheter the user browser support cookies or not
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')


def checkTestCookie(request):
    # check the test cookie get set or not
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')


def deleteTestCookie(request):
    # now we will delete the test cookie
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')
