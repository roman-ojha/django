from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# now only after login user can access this view
@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@login_required
@staff_member_required
def staff(request):
    return render(request, 'registration/staff.html')
