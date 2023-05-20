import django.apps
from django.contrib import admin
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Post
from django import forms

TEXT = "Some text that we can include"


class PostAdmin(admin.ModelAdmin):
    # specifying the fields and the over of fields that we want to display inside the admin site while adding and changing the record data
    # fields = ['title', 'author']

    # Group fields:
    # grouping will display those grouped fields in same row
    # fields = ['title', ('author', 'slug')]

    # Create Sections:
    # now here we will create the fields with different sections
    fieldsets = (
        # ("<name_of_the_section>",{'fields':(<fields_inside_the_section>)})
        ("Section 1", {
            'fields': ('title', 'author'),
            # you can also include descriptions
            'description': '%s' % TEXT,
        }),
        ("Section 2", {
            'fields': ('slug',),
            # you can attached some classes with you sections
            'classes': ('collapse',),
        }),
    )
    # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets

    # Help Text:
    # you can add some text underneath every fields to provide the user some information
    # there is different way to achieve that but one of the way is by using the Model
    # EX: inside the './models.py' on Post model: title = models.CharField(max_length=250, help_text="This is title title")


# admin.site.register(Post, PostAdmin)


# Custom Form:
class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # now bellow here we can define what we want in our form
        self.fields['title'].help_text = "New title help text"

    class Meta:
        model = Post
        exclude = ('slug',)  # exclude the unwanted fields


# Using the Custom form that we create and register it into the admin page
@admin.register(Post)
class PostFormAdmin(admin.ModelAdmin):
    form = PostForm
