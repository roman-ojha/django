from django.shortcuts import render
from .models import Student

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

    return render(request, 'school/home.html', {'students': students})
