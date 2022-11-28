from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='enroll'),
    # 'id' will get pass into views function as keyword argument
    path('student/<id>/', views.show_details, name='detail'),

    # converting 'id' to int
    path('student/int/<int:id>/', views.show_details_int, name='int-detail'),

    # multiple dynamic url
    path('student/int/<int:id>/<int:sub_id>/',
         views.show_sub_details_int, name='int-sub-detail'),

    # passing kwargs
    path('student/',
         views.kwargs_view, kwargs={'id': 5, 'name': "Jack"}, name="student")
]
