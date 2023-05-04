from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


def addAndShow(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(name=name, email=email, password=password)
            user.save()
        fm = StudentRegistration()
        students = User.objects.all()
    else:
        fm = StudentRegistration()
        students = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'students': students})
