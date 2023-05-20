from django.contrib import admin
from . import models


# Creating custom Admin Site
class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    # specifying the custom login template
    login_template = 'blog/admin/login.html'


blog_site = BlogAdminArea(name='BlogAdmin')
blog_site.register(models.Post)
# Now we will proved this admin site using url from '../core/urls.py'

"""
    => After that we will create our own Login Admin template inside '../template/blog/admin' folder
    To use the template you have to add this inside 'settings.py'
        TEMPLATES = [
            {
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
            },
        ]

    *) Collect Default Static files
        => So Now have to use the Static files like CSS, JS, images so we will add the static folder path inside 'settings.py' file
            STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        => And also have to add this code inside the 'urls.py' file
            from django.conf import settings
            from django.conf.urls.static import static
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('blog-admin/', blog_site.urls),
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        => Now we will going to run:
            -> py manage.py collectstatic
                -> this will generate all the default static files inside the '../static' folder, and there are the static files that django admin uses and we can use these static fils to customize the admin site
    *) Customize Template:
        => So, what we can do now is to find the template of the existing admin page & then copy that into you template and then make some changes over there
        => So, because we are trying to override and customize the login page we will first get that default login page from the default django template which exist inside the packages Lib directory './venv/Lib/site-packages/django/contrib/admin/templates/admin/login.html' we will get that template and add it into the '/templates/blog/admin' folder
        => Now inside the "BlogAdminArea" we have 'login_template' now we will specify the custom login template there
    *) Customize CSS:
        => Now we will try to apply custom styling for that we will going to use the default login page css file and add it into '../static/blog/admin/login.css'
        => Now after customizing the 'login.css' file we will now include that css file into the custom 'login.html' file
        => to use custom css files we have to specify the Static file root directory where css will be found so we will add bellow code inside the 'settings.py' file
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'static')
            ]
        => Now we will not going to use 'STATIC_ROOT' variable so we will remove that
"""
