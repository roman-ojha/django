from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # we can use the default 'TemplateView' provided by the django to render the template
    path('', views.TemplateView.as_view(
        template_name='school/home.html'), name='home'),

    # using View defined by us by inheriting 'TemplateView'
    # we can also pass extra context from here that will get pass into template
    path(
        'home/', views.HomeTemplateView.as_view(extra_context={'course': 'Django'}), name="home"),
    path(
        'home2/<int:roll>', views.HomeTemplateView.as_view(extra_context={'course': 'Django'}), name="home")
]
