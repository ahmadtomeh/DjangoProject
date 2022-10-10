from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('myCars', views.myCars),
    path('myRequests', views.myRequests),
]