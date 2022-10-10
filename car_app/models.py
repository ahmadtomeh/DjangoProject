from unicodedata import decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from login_registration_app.models import User
from car_app.city_model import City
from datetime import datetime



# Create your models here.

class PowerSourceManager(models.Manager):
    def power_source_validator(self, postData):
        errors = {}
        if postData['power-source'] == 'None':
            errors['power_source'] = 'Choose power source'
        return errors

class PowerSource(models.Model):
    souce = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PowerSourceManager()

class ManufacturerManager(models.Manager):
    def manufacturer_validator(self, postData):
        errors = {}
        if postData['manufacturer'] == 'None':
            errors['manufacturer'] = 'Choose manufacturer'
        return errors

class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ManufacturerManager()

class CarModelManager(models.Manager):
    def car_model_validator(self, postData):
        errors = {}
        if postData['car-model'] == 'None':
            errors['car_model'] = 'Choose car model'
        return errors

class CarModel(models.Model):
    model = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarModelManager()
    manufacturer = models.ForeignKey(Manufacturer, related_name='car_models', on_delete=models.CASCADE)

class CarManager(models.Manager):
    def car_validator(self, postData):
        errors = {}
        if postData['color'] == 'None':
            errors['color'] = 'Choose color'
        if postData['year'] == 'None':
            errors['year'] = 'Choose year'
        if postData['num-passengers'] == 'None':
            errors['num_passengers'] = 'Choose number of passengers'
        if postData['transmission'] == 'None':
            errors['transmission'] = 'Choose transmission'
        if postData['status'] == 'None':
            errors['status'] = 'Choose status'
        if len(postData['price']) < 1:
            errors['price'] = 'Specify price'
        errors['city'] = City.objects.city_validator(postData)['city']
        errors['power_source'] = PowerSource.objects.power_source_validator(postData)
        errors['car_model'] = CarModel.objects.car_model_validator(postData)
        return errors

class Car(models.Model):
    color = models.CharField(max_length=10)
    year = models.IntegerField(validators=[MinValueValidator(1920), MaxValueValidator(datetime.today().year+1)])
    num_passengers = models.IntegerField(validators=[MinValueValidator(1)])
    transmission = models.CharField(max_length=9)
    status = models.CharField(max_length=4)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    bhp = models.IntegerField()
    features = models.TextField()
    photo = models.CharField(max_length=255)
    is_sold = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarManager()
    advertiser = models.ForeignKey(User, related_name='advertised_cars', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='cars', on_delete=models.CASCADE)
    power_source = models.ForeignKey(PowerSource, related_name='cars', on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, related_name='cars', on_delete=models.CASCADE)

class RequestManager(models.Manager):
    def request_validator(postData):
        errors = {}
        if len(postData['request']) < 1:
            errors['request'] = 'Request cannot be empty'
        return errors

class Request(models.Model):
    request = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RequestManager()
    user = models.ForeignKey(User, related_name='requests', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='requests', on_delete=models.CASCADE)

class ReplyManager(models.Manager):
    def reply_validator(postData):
        errors = {}
        if len(postData['reply']) < 1:
            errors['reply'] = 'Reply cannot be empty'
        return errors

class Reply(models.Model):
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReplyManager()
    request = models.ForeignKey(Request, related_name='replies', on_delete=models.CASCADE)