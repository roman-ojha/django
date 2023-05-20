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
