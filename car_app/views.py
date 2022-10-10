from django.shortcuts import render, redirect
from django.contrib import messages
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

# Create your views here.
