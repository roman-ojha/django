from django.contrib import admin
from .models import Post


class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"


blog_admin_site = BlogAdminArea(name='BlogAdmin')
blog_admin_site.register(Post)

admin.site.register(Post)
