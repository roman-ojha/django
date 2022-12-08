# importing signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# importing User model it will become the sender
from django.contrib.auth.models import User
from django.dispatch import receiver


# defining receiver functions
def login_success(sender, request, user, **kwargs):
    # we get extra 'request' & 'user' from 'user_logged_in' signal
    # if user logged successfully then run this function
    print("------------------------------------")
    print("Logged-in Signal...... Run Intro..")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User", user)
    print("User password: ", user.password)
    print(f'Kwargs {kwargs}')
    # here we can check of the number of time user logged in
    # also we can check of the ip address from user try to logged in
    # or whatever you really want


# we have to connect the signal to the receiver
# manual connection
user_logged_in.connect(login_success, sender=User)


# Connect Using Decorator
# @receiver(<signal>, <sender>)
@receiver(user_logged_out, sender=User)
def logged_out(sender, request, user, **kwargs):
    # run this function when user logout signal get triggered
    print("------------------------------------")
    print("Logged-out Signal...... Run Out..")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User", user)
    print("User password: ", user.password)
    print(f'Kwargs {kwargs}')


@receiver(user_login_failed)
def login_fail(sender, credentials, request, **kwargs):
    # run this function when user try to login and get failed to login
    # we will get extra 'credentials' data which contain the login credentials that user used to login
    print("------------------------------------")
    print("Login Failed Signal...... Run Out..")
    print("Sender: ", sender)
    print("Request: ", request)
    print('Credentials: ', credentials)
    print(f'Kwargs {kwargs}')
