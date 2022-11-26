from django.contrib import admin
from .models import Student


# creating ModelAdmin class
class StudentAdmin(admin.ModelAdmin):
    # we have to pass the filed that we want to see on the admin page
    list_display = ('stuid', 'stuname', 'stuemail', 'stupass')


# registering Model & ModelAdmin class
# admin.site.register(Student, StudentAdmin)

# registering Model using decorator
@admin.register(Student)
class StudentAdminClass(admin.ModelAdmin):
    list_display = ('stuid', 'stuname', 'stuemail', 'stupass')
