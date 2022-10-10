from turtle import pos
from urllib import request
from django.db import models
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
import bcrypt
from django.contrib import messages

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first-name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters.'
        if len(postData['last-name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters.'
        user_bday = datetime.strptime(postData['bday'], '%Y-%m-%d')
        if user_bday > datetime.today():
            errors['past'] = 'Birthday should be in the past!'
        if user_bday > datetime.today() - relativedelta(years=13):
            errors['age'] = 'You must be at least 13 years old!'
        if len(postData['bday']) < 10:
            errors['date'] = 'Enter your birthday.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        for user in User.objects.all():
            if postData['email'] == user.email:
                errors['unique_email'] = 'Email already exists!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if postData['password'] != postData['confirm-password']:
            errors['confirm_password'] = 'Confirmed password does not match with password.'
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors['login'] = 'Invalid credentials!'
        else:
            errors['login'] = 'Invalid credentials!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def all_users():
    return User.objects.all()

def register_errors(request):
    return User.objects.register_validator(request.POST)

def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        id = request.POST['id'],
        first_name = request.POST['first-name'],
        last_name = request.POST['last-name'],
        birthday = request.POST['bday'],
        email = request.POST['email'],
        password = pw_hash
    )
    request.session['first_name'] = request.POST['first-name']
    request.session['email'] = request.POST['email']
    request.session['id'] = request.POST['id']

def login_errors(request):
    return User.objects.login_validator(request.POST)

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    logged_user = user[0]
    request.session['first_name'] = logged_user.first_name
    request.session['email'] = request.POST['email']