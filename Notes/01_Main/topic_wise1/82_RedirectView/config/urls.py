from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(
        template_name='school/home.html'), name="main"),

    # we will redirect to: '' path if someone will come to 'home/', 'index/' path
    path('home/', views.RedirectView.as_view(url='/'), name='home'),
    # redirecting using pattern_name that 'name' that we specify on every url path
    path('index/', views.RedirectView.as_view(pattern_name="main"), name='index'),

    # redirect on other url
    path('yt/', views.RedirectView.as_view(url="https://www.youtube.com/"), name='yt'),
    path('youtube/', views.NewRedirectView.as_view(), name='youtube'),

    # route to pass dynamic url value & redirecting to '<int:pk>/' url using 'SecondNewRedirectView' which uses pattern_name
    path('home/<int:pk>', views.SecondNewRedirectView.as_view(), name='homepk'),
    # because we are using 'pattern_name' rather then url on 'SecondNewRedirectView' that 'pk' that get pass to that url will get redirect with the same 'pk' on '<int:pk>/' url
    path('<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mainpk')
]
