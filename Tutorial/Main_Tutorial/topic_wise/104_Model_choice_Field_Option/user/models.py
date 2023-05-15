from django.db import models

# List of color to use inside the choices
FAV_COLOR = [
    # no here we will define color tuples
    # (<value_that_store_into_database>,<human_readable_name>)
    # Store small value as possible
    ('RED', 'Red'),
    ('BLUE', 'Blue')
]


class Person(models.Model):
    name = models.CharField(max_length=50)
    # for the color field we will going to create the options from which user an only choose those options
    color = models.CharField(max_length=50, choices=FAV_COLOR)

# Django shell example:
# python3 manage.py shell
# >>> from user.models import Person
# >>> Person.objects.create(name='a', color='Yello')
# <Person: Person object (1)>
# >>> Person.objects.filter(id=1).values()
# <QuerySet [{'id': 1, 'name': 'a', 'color': 'Yello'}]> # Here we can see that we are able to store the undefined choices into the database and we can be able to do that rather this options 'choices' options will be utilized by your forms, so whenever you generate a forms from the model it will find the choices and populate into the dropdown entry

# So to solve of getting undesired value saved into the 'Person' table django suggest different method/approach
# where we should define the choice inside the model class and define the suitable name constant for each value


class Person2(models.Model):
    RED = 'RD'
    BLUE = 'BL'
    FAV_COLOR2 = [
        (RED, 'Red'),
        (BLUE, 'Blue')
    ]
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, choices=FAV_COLOR2)
    
# Django shell example:
# ❯ python3 manage.py shell
# >>> from user.models import Person2
# >>> Person2.objects.create(name='a', color=Person2.RED) # now here this approach give little bit more protection
# <Person2: Person2 object (1)>
# >>> Person2.objects.filter(id=1).values()
# <QuerySet [{'id': 1, 'name': 'a', 'color': 'RD'}]>


# Another and I would say more better approach using the django enumeration types that we can use as subclass
# django provide 2 options
# 1. if storing text (models.TextChoices)
# 2. if storing int (models.IntegerChoices)
class Person3(models.Model):
    class Colors(models.TextChoices):
        # <variable_name> = <value_to_store>, '<human_readable_value>'
        RED = 'RD', 'Red'
        BLUE = 'BL', 'Blue'

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, choices=Colors.choices)
    
# Django shell example
# ❯ python3 manage.py shell
# >>> from user.models import Person3
# >>> Person3.objects.create(name='a', color=Person3.Colors.RED)
# <Person3: Person3 object (1)>
# >>> Person3.objects.filter(id=1).values()
# <QuerySet [{'id': 1, 'name': 'a', 'color': 'RD'}]>