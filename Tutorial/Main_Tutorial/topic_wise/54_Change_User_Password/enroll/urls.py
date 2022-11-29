from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.sign_in, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    # change password with required Old password
    path('changepass/', views.user_change_pass, name='changepass'),
    # change password with out required Old password
    path('changepass1/', views.change_pass_with_out_old, name='changepasswoold')
]
