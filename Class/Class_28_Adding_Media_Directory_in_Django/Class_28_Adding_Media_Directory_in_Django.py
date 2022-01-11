"""
-> so the recomended way to store the media are:
    -> first go to 'setting.py' and add some media files
        -> MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        -> MEDIA_URL = '/media/'
    -> now go to project(env) 'urls.py' and we will going to edit the url patterns
        -> import :
            -> from django.conf import settings
                from django.conf.urls.static import static
        -> and in urlpatterns add:
                urlpatterns = [
                path('admin/', admin.site.urls),
                path('shop/', include('shop.urls')),
                path('blog/', include('blog.urls')),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
-> now if we will add the another product in database with the image it will going to add in the media\shop\images\<image.jpg>
-> it means it will create the new folder in root directory 'media'
"""
