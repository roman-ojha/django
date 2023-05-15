from django.shortcuts import render


def show_details(request, year):
    print(year)
    return render(request, 'enroll/show.html', {'year': year})
