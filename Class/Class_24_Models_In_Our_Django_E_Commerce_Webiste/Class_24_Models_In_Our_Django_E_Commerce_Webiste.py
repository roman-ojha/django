"""
# model:
    -> https://docs.djangoproject.com/en/3.2/topics/db/models/
    -> A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
    -> data store in the database but in django, in django we have default sqlite database 'db.sqlite3'
    -> if we go to the 'env' folder under setting.py we can see 'DATABASES' in there
    -> in that 'DATABASES' we can see the default database 
            -> 'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
    # SQlite
        -> SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine
        -> those app that we have in project use some table or database
        -> we get the working while running the server :
                -> You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
                Run 'python manage.py migrate' to apply them.
        -> it is basically saying that we mignt need a tabel(database) for this project which you havenot made, issued the command so that django can make a tables
        -> so the command for that is:
            -> python manage.py migrate
        -> it means those table which is need for the app create them
        -> now after that we can see in our project apps a new folder 'migrations'
        -> here 'migrations' means those change that we made in modle, django will store it
            -> Let's take an EX:
                    -> our table name is 'products' i am changing it to another name 'saman'
                    -> then we will make a migration of that
                    -> if we are making migration then we are not still changed the database
                    -> we had just store the information that we are trying to change
                    -> when we will apply the migration only after that we change it in our database
                    -> after that all the migration will be apply
    
    -> now we go to the models.py of shop app and write some code to make a model

    -> and in the apps like: in 'shop' we have apps.py file where we have class 'ShopConfig' which is automatically given by django
    -> so things that we change in 'env/setting.py' in 'INSTALLED_APPS' we had make use:
        INSTALLED_APPS = [
                'shop',
            ]
        -> but now, we can replace it with :  'shop.apps.ShopConfig'
        -> INSTALLED_APPS = [
                'shop.apps.ShopConfig'
            ]
        -> here we are trageting rather then targating app
    -> now we will write in terminal in :
        -> python manage.py makemigrations (for all app)
        -> python manage.py makemigrations <app_name> (for spacific app)

        -> it will store the migrations
        -> it is detect changes and it is showing like:
            -> Migrations for 'shop':
                shop\migraions\0001_initial.py
                    - create model Product
        -> where it will make a new file '0001_initial.py' in migrations folder
        -> now those store in the migration we can apply it by:
            -> python manage.py migrate
        -> it means we are changing it to database and it will apply the magration
        -> now our sqlite table has been write
        -> how to know or test that it had been write or not
        -> and we can test it by making admin account
        -> and in django admin pannel had already been made we just need to use 3 command and our admin panel will be ready to use
"""
