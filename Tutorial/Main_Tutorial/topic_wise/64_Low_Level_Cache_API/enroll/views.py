from django.shortcuts import render
from django.core.cache import cache


def home(request):
    # get value and pass default if didn't exist
    mv = cache.get('movie', 'has_expired')
    print(mv)
    if mv == 'has_expired':
        # if given key didn't exist on cache then we will set value on cache
        cache.set('movie', 'The Manjhi', 30)
        # get('<key>', '<value>', <second>)
        mv = cache.get('movie')

    # another way rather then write these about of code is:
    fees = cache.get_or_set('fees', 4000, 30)

    # setting version as well so that with the same key we can store different value
    mv = cache.set('fees', 3000, version=2)

    # setting many values at once
    data = {'name': 'roman', 'roll': 25}
    cache.set_many(data, 30)

    # getting many result at once
    # sv = cache.get_many(data)
    sv = cache.get_many(['name', 'roll', 'movie'])
    print(sv)

    # Delete
    cache.delete('name')
    # Delete with version
    cache.delete('fees', version=2)

    # Decrement / Increment
    cache.set('id', 255, 30)
    # decrement by 1
    cache.decr('id', delta=1)
    id = cache.get('id')
    print(id)

    # increment by 2
    cache.incr('id', delta=2)
    id = cache.get('id')
    print(id)

    # Decrement/Increment Version
    # cache.decr_version('roll', delta=1, version=2)
    # cache.incr_version('roll', delta=3, version=2)

    # clear all cache data
    cache.clear()

    return render(request, 'enroll/course.html', {'fm': mv, 'fees': fees})
