from django.contrib import admin
from .models import Post


class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"


blog_admin_site = BlogAdminArea(name='BlogAdmin')
# Now we registered this Admin area after that we will go to '../core/urls.py' to access this site

# Also we will going to create the new model for this app './models.py' and registered that here
# But while registering the site now we will not going to use the main 'admin' rather we will use the custom admin that we just create 'blog_admin_site'
blog_admin_site.register(Post)

# also we will going to register this mode into main admin site
admin.site.register(Post)

# here we will create the custom AdminConfig
