from django.shortcuts import render
from .forms import UserRegistration
from .models import User


def register(request):
    if request.method == "POST":
        # to update the data we will first get the data
        # so updating the data that have id = 2
        pi = User.objects.get(pk=2)

        # by passing the instance into the ModelForm it will bind those value that user enter with the model and now we can update that data
        form = UserRegistration(request.POST, instance=pi)

        # on update
        operation = 'update'

        # on save
        # operation = 'save'

        if form.is_valid():
            if operation is 'save':
                # saving the data
                print(form.cleaned_data)
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                reg = User(name=name, email=email, password=password)
                reg.save()
            else:
                # updating the data
                form.save()
    else:
        form = UserRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
