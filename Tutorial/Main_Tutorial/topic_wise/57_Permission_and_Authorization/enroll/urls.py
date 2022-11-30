from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.sign_in, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'),

    # route to render specific user user passed id
    path('userdetail/<int:id>/', views.user_detail, name='userdetail')
]
