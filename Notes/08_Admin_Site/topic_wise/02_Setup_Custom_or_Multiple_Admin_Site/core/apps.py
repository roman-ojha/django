from django.contrib.admin.apps import AdminConfig


# here we will configure and the new Admin Configuration
class BlogAdminConfig(AdminConfig):
    # and specify the default Admin Site class
    default_site = "blog.admin.BlogAdminArea"
    # default_site = "<app_name>.admin.<admin_site_class_name>"
