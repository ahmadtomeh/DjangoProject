from django.shortcuts import render, redirect
from django.contrib import messages
<<<<<<< HEAD
from . import models

def home(request):
    return render(request, 'home.html')

def showCar(request):
    return render(request, 'showCar.html')

def myCars(request):
    return render(request, 'myCars.html')

def myRequests(request):
    return render(request, 'myRequests.html')

def requestCar(request):
    return render(request, 'requestCar.html')

def postComment(request):
    return render(request, 'post&comment.html')
=======
from . import models, city_model
>>>>>>> 4f77f5a6c7fa2cea2137bc0bcf91e4fbe7edfa51

def index(request):
    return render(request, 'city.html')

def city(request):
    errors = city_model.City.objects.city_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/car')
    return redirect('/car/success')

def success(request):
    return render(request, 'success.html')