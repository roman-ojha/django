from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# We will going to create the custom user model
# We should not use the default use model but rather extend it using 'AbstractUser'
# 'AbstractUser' will have to exact replication of actual default django user model and it's feature
class User(AbstractUser):
    # Create the roles
    class Role(models.TextChoices):
        # define different users
        ADMIN = "ADMIN", 'Admin'  # 'Admin' is the human readable
        STUDENT = "STUDENT", 'Student'
        TEACHER = "TEACHER", 'Teacher'

    # define base/default role
    base_role = Role.ADMIN

    # here we want to all a role with given choices like: 'Admin', 'Student' & 'Teacher'
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        # while saving the User we want to assign the custom roles here so we over ride the 'save' method
        if not self.pk:  # user have not been created
            self.role = self.base_role
            # after assigning default roles we will going to save the user
            return super().save(*args, **kwargs)

# Because we are using the custom Auth user model we have to configure that into 'settings.py' file:
# AUTH_USER_MODEL = "user.User"


# Defining the custom Student manager
class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        # we will find the user data and only return the Student data
        return results.filter(role=User.Role.STUDENT)

# Example which shows while querying suing 'student' manager we will only get the data having 'role' as 'STUDENT'
# ❯ python manage.py shell
# >>> from user.models import Student
# >>> Student.student.all()
# <QuerySet [<Student: s1>]>
# >>> Student.objects.all() # getting all user data
# <QuerySet [<Student: roman>, <Student: s1>]>

# Now we will define the different Profile model for different type of the user so that they can have different kind of data
# EX: Student user could have it's own different fields/data, Teacher user could have it's own different fields/data
# So, now we will store those data into different table and add relation with the User table
class StudentProfile(models.Model):
    # one to one relation with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # now add field that only Student could have
    student_id = models.IntegerField(null=True, blank=True)


# Now we will create the Student mode that will extend the custom 'User' model
class Student(User):
    # so now here we will define the default role as Student
    base_role = User.Role.STUDENT

    class Meta:
        # proxy True means this is the class which table won't get generated but we can walk through this table when working with student data
        proxy = True

    def welcome(self):  # defining method only for Student
        return "Only for students"

    # Also we can now create the student manager so that we can query the Student model objects and get only the data of students
    student = StudentManager()
    
    # So because we have to different Profile table for S


# Shell example to create new student with 'STUDENT' role:
# python manage.py shell
# >>> from user.models import Student
# >>> Student.objects.create_user(username='s1', password='123@roman')
# <Student: s1>



# Defining the custom Teacher manager
class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)

# Creating Teacher from the same User model
class Teacher(User):
    # so now here we will define the default role as TEACHER
    base_role = User.Role.TEACHER

    class Meta:
        proxy = True

    teacher = StudentManager()

    def welcome(self):
        return "Only for Teacher"
    
# Shell example:
# ❯ python manage.py shell
# >>> from user.models import Teacher
# >>> Teacher.objects.create_user(username='teacher123', email='', password='teacher@123')
# <Teacher: teacher123>
# >>> Teacher.teacher.all()
# <QuerySet [<Teacher: s1>]>
# >>> Teacher.objects.all()
# <QuerySet [<Teacher: roman>, <Teacher: s1>, <Teacher: teacher123>]>