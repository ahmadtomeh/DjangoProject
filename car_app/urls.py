from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home),
    path('myCars', views.myCars),
    path('myRequests', views.myRequests),
=======
    path('', views.index),
    path('city', views.city),
    path('success', views.success),
>>>>>>> 4f77f5a6c7fa2cea2137bc0bcf91e4fbe7edfa51
]