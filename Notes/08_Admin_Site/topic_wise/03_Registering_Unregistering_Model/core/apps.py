from django.contrib.admin.apps import AdminConfig


class BlogAdminConfig(AdminConfig):
    default_site = "blog.admin.BlogAdminArea"
