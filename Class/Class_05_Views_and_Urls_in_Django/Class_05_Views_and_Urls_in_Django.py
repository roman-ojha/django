"""
-> now first run the server using:
    -> python .\manage.py runserver
-> and then on the urls.py file import views:
    -> from . import views
-> and on urlpatterns : wirte path
    -> path('',views.index,name='index')
    -> here '' this is use for the home url and we are connecting the home url with the views.py and 'views.index' will run is the function that will going to run on that given url
    -> and 'name' is for for the path name
-> now on views.py you can use request and respond 
-> here first python/django will go to the url.py and run the home '' url if exist
"""