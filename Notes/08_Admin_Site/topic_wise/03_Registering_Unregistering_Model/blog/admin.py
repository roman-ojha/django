import django.apps
from django.contrib import admin
# Importing the model
from .models import Post
from .models import Category

# Registering the model
# admin.site.register(Post)
admin.site.register(Category)


# Customization of registered model
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author']


# admin.site.register(Post, PostAdmin)

# another way to register model
# @admin.register(Post)
# class Post2Admin(admin.ModelAdmin):
#     fields = ['title', 'author']


# Registering All models
# collect all the models
models = django.apps.apps.get_models()  # this return all the available models

# loop through all the models
for model in models:
    try:
        # now here we will register the model
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        # but we know that some model had already been registered so, we can't register those model again
        # so we will no register those models
        pass


# Unregister Model
admin.site.unregister(django.contrib.sessions.models.Session)
