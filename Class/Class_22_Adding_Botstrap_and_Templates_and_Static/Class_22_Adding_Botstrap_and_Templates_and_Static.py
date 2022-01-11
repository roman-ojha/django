"""
-> First make a folder 'templates' in all app
-> NOTE: blog and shop is app and env is the porject

-> now again insid the blog/template make blog folder
-> and in shop/template make shop folder

-> now we have to put the app inside the INSTALLED_APPS app in setting.py inside env folder
-> now open env/setting.py and in INSTALLED_APPS add:
    -> INSTALLED_APPS = [
                'blog',
                'shop',
            ]

-> now create the template file inside the blog and shop folder
-> here create index.html in blog/templates/blog
-> and add index.html in views.py

# How to run static directory in django
    -> now go the the apps folder and add static folder
    -> in shop add static folder and again inside the static folder create shop folder
    -> do the same thing in blog app as well
    -> now all the static file will come under the static/<app> folder
    -> now create the static file in this case we are creating mystatic.txt inside the blog/static/blog folder
    -> now to add the static file in the index.html you can do this:
        -> {% load static %}
    -> and to use the data of the static file in this case 
        -> <a href="{%static 'blog/mystatic.txt'%}">Click Me</a>
        -> <img src="{%static 'blog/image.png'%}" />
    -> now go the the views.py file in the app 
"""
