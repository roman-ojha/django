"""
    -> now we will create a tweets app:
        -> ./manage.py startapp tweets

    -> by djanog models in default every document will get their own id by default:
        -> models.AutoField(primary_key=True)

    -> now we will create a model in models.py

    -> now will add to project settings.py:
        -> INSTALLED_APPS = [
                    'tweets',
                ]
        -> .\manage.py makemigrations
        -> python manage.py migrate
"""
