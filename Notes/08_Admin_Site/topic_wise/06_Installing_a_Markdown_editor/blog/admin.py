from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    login_template = 'blog/admin/login.html'


blog_site = BlogAdminArea(name='BlogAdmin')


# Creating the custom SummerNote Admin
class SummerAdmin(SummernoteModelAdmin):
    # Specifying the fields that we want to apply on
    summernote_fields = '__all__'  # add summernotes to all fields
    # or also if you want to apply this to Post.content field you can specify this
    # summernote_fields = 'content'


# Now we will install the SummerNote into default Admin Site
admin.site.register(models.Post, SummerAdmin)
# Adding SummerNote to our Custom Admin site
blog_site.register(models.Post, SummerAdmin)
