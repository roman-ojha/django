from django.urls import path
from registration import views

urlpatterns = [
    path("", views.profile, name="profile"),
]
