from django.db import models
from datetime import datetime

class Contacts(models.Model):
    car = models.CharField(max_length=200)
    car_id = models.IntegerField()
    name = models.CharField(max_length=200)    
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    
    def __str__(self):
        return self.name
