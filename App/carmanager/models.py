from django.db import models
from datetime import datetime

class CarManager(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    phone3 = models.CharField(max_length=20)
    # email = models.EmailField()
    email = models.CharField(max_length=200)   
    hire_date = models.DateTimeField(default=datetime.now,blank=True)
    position = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name

