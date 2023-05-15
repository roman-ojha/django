from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Create your views here.


def home(request):
    # Getting all the data from table
    students = Student.objects.all()
    print(students)
    # if you want to see the SQL query that this method is generating then you can use this:
    print("SQL Query: ", students.query)

    # Filter method to return by passing parameters:
    students = Student.objects.filter(marks=300)
    # getting all the student whose marks is 300

    # Exclude:
    students = Student.objects.exclude(marks=300)
    # getting all the student whose marks is not 300

    # OrderBy:
    # getting all the student order by roll
    # Ascending order:
    students = Student.objects.order_by('roll')
    # Descending order:
    students = Student.objects.order_by('-roll')
    # Random order:
    students = Student.objects.order_by('?')
    # NOTE: it order based on unicode
    # Order Ex: A, B, ....., Z, a, b, ...., z
    # Reverse Order:
    students = Student.objects.order_by('id').reverse()
    # Limit: First 2
    students = Student.objects.order_by('id').reverse()[:2]

    # Values:
    students = Student.objects.values()
    # Getting all the students from table in dictionary list
    students = Student.objects.values('name', 'city')
    # Getting all the students name & city from table in dictionary list

    # Values_List:
    students = Student.objects.values_list()
    students = Student.objects.values_list('name', 'city')
    # it return Tuple
    students = Student.objects.values_list('name', 'city', named=True)
    # return named tuple
    # <QuerySet [('roman', 'kathmandu'), ('razz', 'kathmandu'), ('Jack', 'Mumbai')]>

    # Using: if you use multiple database and want to specify from which database you want to query in that case we can use 'using'
    # the name that we specify on the 'setting.py' file is the name of database that we will specify here
    """ 
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    """
    students = Student.objects.using('default')
    students = Student.objects.using('default').all()

    # Dates:
    students = Student.objects.dates('pass_date', 'month')
    print(students)

    # Union:
    # using 'Student' & 'Teacher' models to perform union
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    students = qs2.union(qs1)
    # Getting both 'Student' & 'Teacher' data and union it to get both data into one
    # also it wil remove the duplicate data
    # SELECT "school_teacher"."id", "school_teacher"."name" FROM "school_teacher" UNION SELECT "school_student"."id", "school_student"."name" FROM "school_student"
    students = qs2.union(qs1, all=True)
    # getting duplicate data as well

    # Intersection
    students = qs2.intersection(qs1)
    # return similar data on both Table

    # Difference
    students = qs2.difference(qs1)
    students = qs1.difference(qs2)

    # AND:
    students = Student.objects.filter(id=2) & Student.objects.filter(roll=30)
    students = Student.objects.filter(id=2, roll=30)
    students = Student.objects.filter(Q(id=2) & Q(roll=30))
    # OR:
    students = Student.objects.filter(id=2) | Student.objects.filter(marks=300)
    students = Student.objects.filter(Q(id=2) | Q(marks=300))
    # SELECT "school_student"."id", "school_student"."name", "school_student"."roll", "school_student"."city", "school_student"."marks", "school_student"."pass_date" FROM "school_student" WHERE ("school_student"."id" = 2 OR "school_student"."marks" = 300)

    return render(request, 'school/home.html', {'students': students})
