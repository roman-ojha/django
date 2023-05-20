from django.contrib import admin
from django.urls import path, include
from blog.admin import blog_site
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-admin/', blog_site.urls),
    path('summernote/', include('django_summernote.urls'))
]

# When we are in debug mode we will going to utilize the Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
