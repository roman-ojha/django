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
]
