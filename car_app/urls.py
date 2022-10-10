from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('city', views.city),
    path('success', views.success),
]