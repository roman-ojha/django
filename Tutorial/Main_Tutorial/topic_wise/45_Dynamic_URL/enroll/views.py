from django.shortcuts import render


def home(request):
    return render(request, 'enroll/home.html')


def show_details(request, id=1):
    # getting 'id' from dynamic urls value
    # we can use **kwargs as well to get the dynamic urls values
    # we can also define the default value if the value didn't came from url
    print(id)
    return render(request, 'enroll/show.html', {'id': id, "name": "Null"})


def show_details_int(request, id):
    # using id as int
    if id == 1:
        return render(request, 'enroll/show.html', {'id': id, 'name': "Roman"})
    if id == 2:
        return render(request, 'enroll/show.html', {'id': id, 'name': "Razz"})
    return render(request, 'enroll/show.html', {'id': id, "name": "Null"})


def show_sub_details_int(request, id, sub_id):
    # using id as int
    if id == 1 and sub_id == 2:
        return render(request, 'enroll/show.html', {'id': id, 'name': "Roman"})
    if id == 2 and sub_id == 1:
        return render(request, 'enroll/show.html', {'id': id, 'name': "Razz"})
    return render(request, 'enroll/show.html', {'id': id, "name": "Null"})


def kwargs_view(request, id, name):
    # getting 'id' from kwargs
    return render(request, 'enroll/show.html', {'id': id, "name": name})
