from django.db import models
from datetime import datetime

class Blog(models.Model):
    author = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=500, default=True)
    article = models.CharField(max_length=1500)
    publish_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.author
