from django.dispatch import Signal, receiver

# Creating signal
# name of the signal
notification = Signal(["request", "user"])


# Receiver Function
# using 'notification' signal
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")
