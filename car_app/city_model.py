from email.policy import default
from django.db import models

class CityManager(models.Manager):
    def city_validator(self, postData):
        errors = {}
        if postData['city'] == 'None':
            errors['city'] = 'Choose city'
        return errors

class City(models.Model):
    name = models.CharField(max_length=10, null=True, default='Nablus')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = CityManager()