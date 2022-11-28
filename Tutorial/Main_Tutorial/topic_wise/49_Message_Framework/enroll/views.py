from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            # after we register the user and save it into database we will create the message saying register successfully
            # and then we will show that message to the template

            # adding message
            messages.add_message(request, messages.SUCCESS,
                                 'Your Account has been created !!!')
            # now this message will automatically pass to the template file that we rendered

            # different way to send the message
            messages.info(request, "Now you can log in !!!")

    else:
        form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
