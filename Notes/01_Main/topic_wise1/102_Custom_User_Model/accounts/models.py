from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# First we will create the custom User Manager
class CustomUserManager(BaseUserManager):
    # to create the user we will use 'email' rather then default username field
    # **extra field that comes with the default user model
    def create_user(self, email, password, **extra_fields):
        # function responsible for creating a custom user
        # getting email but we will use the 'normalize_email' function which will turn the string into valid email
        email = self.normalize_email(email)
        # creating the user object
        user = self.model(
            email=email,
            **extra_fields
        )
        # we will set the provided password
        user.set_password(password)
        # saving the user object
        user.save()
        return user

    # function to create super user
    def create_superuser(self, email, password, **extra_fields):
        # this function contain how we will going to create the super user
        # while creating the super user we will going to set the default value for some fields
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # to create a super user we will check/validate some fields
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being true")

        # after that we will call the 'create_user' function which will create user for us
        return self.create_user(email=email, password=password, **extra_fields)


# Defining the User model
# We will use the 'AbstractUser' class if we want to create user model that's custom and has all the other existing django user model fields
class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)
    # Here we have defined our own custom fields
    # Also we have inherited from 'AbstractUser' class it because of that all the other 'extra_fields' will get provided to this model
    # Like: 'is_superuser', 'first_name', 'is_staff', 'is_active', 'user_permissions'

    # so we will now going to add our created custom manager
    objects = CustomUserManager()

    # we will use 'email' as our username field
    USERNAME_FIELD = "email"
    # also we have to define some fields as require like 'username'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:  # string representation of user object
        return self.username

# After create the custom user model we have to tell Django that we have Custom User model created and use that Model as the User auth model for authentication
# for that we will add this in 'settings.py' file:
# AUTH_USER_MODEL = "accounts.User"

# Also we will register our custom User model to admin inside './admin.py'

# now we will migrate
# and create the super user with email & password
