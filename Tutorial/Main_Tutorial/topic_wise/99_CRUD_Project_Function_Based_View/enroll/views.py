from django.shortcuts import render


def addAndShow(request):
    return render(request, 'enroll/addandshow.html')
