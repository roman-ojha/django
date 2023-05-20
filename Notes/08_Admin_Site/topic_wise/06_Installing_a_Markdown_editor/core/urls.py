from django.contrib import admin
from django.urls import path
from blog.admin import blog_site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-admin/', blog_site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
