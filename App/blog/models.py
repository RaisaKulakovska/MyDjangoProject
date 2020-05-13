from django.db import models
from datetime import datetime

class Blog(models.Model):
    author_id = models.IntegerField(default=True)    
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=500, default=True)
    article = models.CharField(max_length=1500)
    publish_date = models.DateTimeField(default=datetime.now,blank=True)
    article_photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.author_id
