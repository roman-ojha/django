from django.shortcuts import render
from .forms import StudentRegistration


def register(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
