from django.shortcuts import render
from .forms import StudentRegistration


def showFormData(request):
    # auto_id:
    form = StudentRegistration(auto_id='some_%s')
    # Output: <input type="text" name="name" required id="some_name">

    form = StudentRegistration(auto_id=True)
    # Output: <input type="text" name="name" required id="name">
    form = StudentRegistration(auto_id='anyString')
    # Output: <input type="text" name="name" required id="name">

    form = StudentRegistration(auto_id=False)
    # will remove label tag and:
    # Output: <input type="text" name="name" required>

    # label_suffix:
    form = StudentRegistration(auto_id=True, label_suffix='')
    # Output: <label for="name">Name</label>

    form = StudentRegistration(auto_id=True, label_suffix='/roman')
    # Output: <label for="name">Name/roman</label>

    # initial:
    form = StudentRegistration(
        auto_id=True, label_suffix=' ', initial={'name': 'roman'})
    # Output: <input type="text" name="name" value="roman" required id="name">
    form = StudentRegistration(
        auto_id=True, label_suffix=' ', initial={'name': 'roman', 'email': 'roman@gmail.com'})

    form = StudentRegistration(
        auto_id=True, label_suffix=' ', initial={'name': 'roman'})
    return render(request, 'enroll/registration.html', {'form': form})
