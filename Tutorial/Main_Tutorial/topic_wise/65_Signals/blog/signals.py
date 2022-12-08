# importing signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete
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
    print("Login Failed Signal......")
    print("Sender: ", sender)
    print("Request: ", request)
    print('Credentials: ', credentials)
    print(f'Kwargs {kwargs}')
# user_login_failed.connect(login_fail)


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    # function that will get called before the new instance of mode being saved
    print("------------------------------------")
    print("Pre Save Signal....")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f'Kwargs {kwargs}')
# pre_save.connect(at_beginning_save,sender=User)


@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    # function that will get called after the new instance of mode get saved
    if created:
        # if record is being created
        print("------------------------------------")
        print("Post Save Signal....")
        print("New Record")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print(f'Kwargs {kwargs}')
    else:
        # if record is being update
        # we can renew the cache if user Update
        print("------------------------------------")
        print("Post Save Signal....")
        print("Update")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print(f'Kwargs {kwargs}')
# post_save.connect(at_ending_save, sender=User)


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    # function that will get called before the model is being delete
    print("------------------------------------")
    print("Pre Delete Signal....")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f'Kwargs {kwargs}')
# pre_delete.connect(at_beginning_delete,sender=User)


@receiver(pre_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    # function that will get called after the model is get deleted
    print("------------------------------------")
    print("Post Delete Signal....")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f'Kwargs {kwargs}')
# post_delete.connect(at_ending_delete, sender=User)


@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    # function that will get called whenever the new django model is being instantiate
    print("------------------------------------")
    print("Pre Init Signal....")
    print("Sender: ", sender)
    print(f'Args {args}')
    print(f'Kwargs {kwargs}')
# pre_init.connect(at_beginning_init, sender=User)


@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    # function that will get called whenever the new django model is being instantiate
    print("------------------------------------")
    print("Post Init Signal....")
    print("Sender: ", sender)
    print(f'Args {args}')
    print(f'Kwargs {kwargs}')


post_init.connect(at_ending_init, sender=User)
