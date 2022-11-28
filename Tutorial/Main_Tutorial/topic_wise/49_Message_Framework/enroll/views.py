from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # form.save()
            # after we register the user and save it into database we will create the message saying register successfully
            # and then we will show that message to the template

            # adding message
            messages.add_message(request, messages.SUCCESS,
                                 'Your Account has been created !!!')
            # now this message will automatically pass to the template file that we rendered

            # different way to send the message
            messages.info(request, "Now you can log in !!!")

            # getting level
            print(messages.get_level(request))
            # return: 20
            # by default we can't see the level below 20 or from below INFO
            # until we set the debug level

            # can't get level for debug before we set the level
            messages.debug(request, "We are in Debug environment before set")

            # setting level
            messages.set_level(request, messages.DEBUG)

            # now we can see this debug message into the template
            messages.debug(request, "We are in Debug environment after set")

            # now getting debug
            print(messages.get_level(request))
            # return: 10

            # sending other messages
            messages.warning(request, "This is warning")

            # we had change the message tag name of error to danger in 'settings.py'
            # EX: MESSAGE_TAGS = { msg.ERROR: 'danger'}
            messages.error(request, "This is error")

            # if we want to get the message inside the python file rather then in template then we can use this
            storage = messages.get_messages(request)
            for message in storage:
                print(message)

    else:
        form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
