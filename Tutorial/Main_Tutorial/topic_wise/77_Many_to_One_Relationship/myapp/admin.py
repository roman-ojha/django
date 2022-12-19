from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title',
                    'post_cat', 'post_published_date', 'user']
