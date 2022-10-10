from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('/check_register', views.check_register),
    path('/check_login', views.check_login),
    path('/logout', views.logout),
]