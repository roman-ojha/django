import django.apps
from django.contrib import admin
from .models import Post
from .models import Category

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author']


admin.site.register(Post, PostAdmin)

models = django.apps.apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


admin.site.unregister(django.contrib.sessions.models.Session)
