from django.urls import path
from . import views

urlpatterns = [
    # Using Function Based View
    path('func/', views.myView, name='func'),

    # Using Class Based View
    # path('class/', views.MyView.as_view(), name="class"),
    # we can also pass as value into class based view from here
    path('class/', views.MyView.as_view(get_data="Class based view - GET"), name="class"),
    path('subclass/', views.MyViewChild.as_view(
        get_data="Class based view - GET, Subclass"), name="subclass"),

    # return render function with context
    path('homefunc/', views.homeFunc, name='homefunc'),
    path('homeclass/', views.HomeClass.as_view(), name='homeclass'),

    # return form data
    path('contactfunc/', views.contactFun, name='contactfun'),
    path('contactclass/', views.ContactClass.as_view(), name='contactclass'),

    # rendering different template file using same view function
    path('newsfunc/', views.newsFun,
         {'template_name': 'school/news.html'}, name='newsfunc'),
    path('newsfunc2/', views.newsFun,
         {'template_name': 'school/news2.html'}, name='newsfunc2'),
    path('newsclass/', views.NewsClass.as_view(template_name='school/news.html'),
         name='newsclass'),
    path('newsclass2/', views.NewsClass.as_view(template_name='school/news2.html'),
         name='newsclass2'),
]
