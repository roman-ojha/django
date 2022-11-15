"""
    Write in terminal:
        -> django-admin 
        -> if it don't work then create the venv in the root directory and then install the django there:
            -> go to directory and then create venv
                -> python -m venv environment
            -> and then go to :
                -> environment\Scripts\activate
                -> to deactivate environment:
                    -> deactivate
            -> and then install django:
                -> pip install django
            -> and then write :
                -> django-admin (i thing it has to work)
    -> now you can see that all avilable cammand
        ->  check
            compilemessages
            createcachetable
            dbshell
            diffsettings
            dumpdata
            flush
            inspectdb
            loaddata
            makemessages
            makemigrations
            migrate
            runserver
            sendtestemail
            shell
            showmigrations
            sqlflush
            sqlmigrate
            sqlsequencereset
            squashmigrations
            startapp
            startproject
            test
            testserver
    -> now create a project
        -> django-admin startproject djangoenv
    -> it generate the file/folder name :
        -> <project_name>
            manage.py
        -> <project_name> folder:
                -> __init__.py
                    -> it will be empty
                -> setting.py
                    -> all the setting avilable in the file
                -> urls.py
                    -> here will be the decleration of url
                -> wsgi.py (webserver getway interface)

    -> to run the server:
        -> python manage.py runserver

            -> if migration problem:
                -> python manage.py makemigrations
                -> python manage.py migrate
    -> and open the website on:
        -> http://127.0.0.1:8000/
"""