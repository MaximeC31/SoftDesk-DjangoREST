from django.urls import path
from .views import register_user, profile

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("profile/", profile, name="profile"),
]
