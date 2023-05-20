"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.admin import blog_admin_site
from bookstore.admin import bookstore_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # now we can access the Blog Admin area inside the '/blog-admin' url path
    path('blog-admin/', blog_admin_site.urls),
    path('bookstore-admin/', bookstore_site.urls),
]

# Change admin title page
# admin.site.index_title = "The Bookstore"
# admin.site.site_header = "The Bookstore Admin"
# admin.site.site_title = "Site Title Bookstore"
