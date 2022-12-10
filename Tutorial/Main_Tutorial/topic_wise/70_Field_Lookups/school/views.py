from django.shortcuts import render
from .models import Student
from datetime import date, time


def home(request):
    students = Student.objects.filter(name__exact='roman')

    students = Student.objects.filter(name__iexact='roman')
    # i for case insensitive

    students = Student.objects.filter(name__contains='zz')

    students = Student.objects.filter(name__icontains='zz')

    students = Student.objects.filter(id__in=[1, 2, 5])
    # those how have id as given

    students = Student.objects.filter(marks__in=[300, 500])

    # greater then:
    students = Student.objects.filter(marks__gt=300)

    # greater then or equal:
    students = Student.objects.filter(marks__gte=300)

    # less then:
    students = Student.objects.filter(marks__lt=500)

    # less then or equal:
    students = Student.objects.filter(marks__lte=500)

    # starts with:
    students = Student.objects.filter(name__startswith='r')
    students = Student.objects.filter(name__istartswith='r')

    # ends with:
    students = Student.objects.filter(name__endswith='n')
    students = Student.objects.filter(name__iendswith='n')

    # range:
    students = Student.objects.filter(
        pass_date__range=('2012-04-14', '2022-05-01'))

    # date:
    students = Student.objects.filter(
        admdatetime__date=date(2022, 12, 10))
    # date with greater then
    students = Student.objects.filter(
        admdatetime__date__gt=date(2022, 12, 9))
    # we can add these multiple lookup in ever other field lookup

    # year:
    students = Student.objects.filter(
        pass_date__year=2022)
    # year greater then
    students = Student.objects.filter(
        pass_date__year__gt=2020)

    # month:
    students = Student.objects.filter(
        pass_date__month=10)
    students = Student.objects.filter(
        pass_date__month__gt=4)

    # day:
    students = Student.objects.filter(
        pass_date__day=2)
    students = Student.objects.filter(
        pass_date__day__gt=3)
    students = Student.objects.filter(
        pass_date__day__gte=3)

    # week:
    students = Student.objects.filter(
        pass_date__week=14)

    # week day:
    students = Student.objects.filter(
        pass_date__week_day=3)
    students = Student.objects.filter(
        pass_date__week_day__gt=3)

    # quarter:
    students = Student.objects.filter(
        pass_date__quarter=3)

    # time
    students = Student.objects.filter(
        admdatetime__time__gt=time(6, 00))

    # hour:
    students = Student.objects.filter(
        admdatetime__hour__gt=5)

    # minute:
    students = Student.objects.filter(
        admdatetime__minute__gt=56)

    # second
    students = Student.objects.filter(
        admdatetime__second__gt=20)

    # isnull
    students = Student.objects.filter(
        admdatetime__isnull=False)

    print("SQL: ", students.query)
    return render(request, 'school/home.html', {'students': students})
