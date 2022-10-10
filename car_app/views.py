from django.shortcuts import render, redirect
from django.contrib import messages
from . import models, city_model

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