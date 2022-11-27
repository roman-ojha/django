from django.shortcuts import render
from .forms import StudentRegistration


def register(request):
    if request.method == "POST":
        # if method is POST then we will validate and then save into database
        form = StudentRegistration(request.POST)
        # we can access the data that use send on POST request like this as well
        print(request.POST['name'])
        print(request.POST['email'])
        print(request.POST['password'])
        print(request.POST['csrfmiddlewaretoken'])
        # But these data aren't a 'cleaned_data' or not a validate data so rather first validate the data then access then validated data

        if form.is_valid():
            # we can access the 'clean_data' after from get valid
            print(form.cleaned_data)
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
            # Now you can save data into database

    else:
        # on GET request we will just send the blank form
        form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
