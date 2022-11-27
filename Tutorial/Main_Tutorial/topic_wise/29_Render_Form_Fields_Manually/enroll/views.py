from django.shortcuts import render
from .forms import StudentRegistration


def showFormData(request):
    form = StudentRegistration()
    form.order_fields(field_order=['first_name', 'name', 'email'])
    # Output:
    # <input type="text" name="first_name" required id="id_first_name">
    # <input type="text" name="name" required id="id_name">
    # <input type="email" name="email" required id="id_email">

    form = StudentRegistration(field_order=['name', 'first_name', 'email'])
    # Output:
    # <input type="text" name="name" required id="id_name">
    # <input type="text" name="first_name" required id="id_first_name">
    # <input type="email" name="email" required id="id_email">
    return render(request, 'enroll/registration.html', {'form': form})
