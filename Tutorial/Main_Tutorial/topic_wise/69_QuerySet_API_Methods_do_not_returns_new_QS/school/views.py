from django.shortcuts import render
from .models import Student


def home(request):
    # get:
    # get single data base on primary key
    # also every row need to be uniquely identify with the from which we are trying to query
    # also it need to match the data that we are trying to query
    student = Student.objects.get(pk=1)
    # we know id is also unique
    student = Student.objects.get(id=2)
    # we make roll unique as well
    student = Student.objects.get(roll=25)

    # first:
    # get the first match data
    student = Student.objects.first()
    student = Student.objects.order_by('name').first()
    student = Student.objects.order_by('-name').first()
    student = Student.objects.filter(roll=25).first()

    # last:
    student = Student.objects.last()
    student = Student.objects.order_by('name').last()
    student = Student.objects.order_by('-name').last()
    student = Student.objects.filter(roll=25).last()

    # latest:
    student = Student.objects.latest('pass_date')

    # earliest
    student = Student.objects.earliest('pass_date')

    # exists:
    # check does data or not
    student = Student.objects.all()
    print(student.exists())
    print(student.filter(pk=Student.objects.get(pk=1).pk).exists())

    # Create:
    # to create|insert data
    # student = Student.objects.create(
    #     name='Tony', roll=33, city="Kathmandu", marks=321, pass_date='2020-5-4')

    # get_or_create:
    # get if exist if not then create
    student, created = Student.objects.get_or_create(
        name='Tony', roll=33, city="Kathmandu", marks=321, pass_date='2020-5-4')

    # update:
    # to update the data
    # NOTE: update method only work on QuerySet not only object
    # update single data
    student = Student.objects.filter(id=2).update(name="Razz Roman", marks=421)
    # update multiple data
    student = Student.objects.filter(marks=421).update(name="Razz", marks=500)

    # update or create
    # update if exist if not create
    # student, created = Student.objects.update_or_create(
    #     id=4, name='Tony', defaults={'name': 'tony', 'roll': 30, 'city': "Kathmandu", 'marks': 321, 'pass_date': '2020-5-4'})
    # if id=4 and name = 'Tony' exist then update 'defaults'

    # bulk_create:
    # create multiple data at once
    objs = [
        Student(
            name='Strange', roll=21, city="Kathmandu", marks=321, pass_date='2020-5-4'),
        Student(
            name='Superman', roll=22, city="Pokhara", marks=123, pass_date='2020-4-4'),
    ]
    # students = Student.objects.bulk_create(objs=objs)

    # bulk_update:
    all_students = Student.objects.all()
    for stu in all_students:
        # assign value here to update
        if stu.marks == 300:
            print(stu.marks)
            stu.city = "New York"
    # update those assigned bulk data
    students = Student.objects.bulk_update(all_students, ['city'])

    # in_bulk:
    # get in bulk:
    students = Student.objects.in_bulk([1, 2])
    # get data which have primary key 1,2
    print(students)
    students = Student.objects.in_bulk([])
    # return empty dictionary
    students = Student.objects.in_bulk()
    # return all

    # delete:
    # student = Student.objects.get(pk=18).delete()
    # delete single record
    # student = Student.objects.filter(marks=500).delete()
    # delete multiple record
    # student = Student.objects.all().delete()
    # delete all record

    # count:
    # count all the output records
    students = Student.objects.all()
    print(students.count())

    # explain:
    return render(request, 'school/home.html', {'student': student})
