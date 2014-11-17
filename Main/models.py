from django.db import models
from datetime import datetime


class DeathBlog(models.Model):
    
    title = models.CharField(max_length=255)
    post_date = models.DateTimeField(default=datetime.now, editable=True)
    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.CharField(max_length=100000)


class DeathFeed(models.Model):
    title = models.CharField(max_length=255)
    vid_id = models.IntegerField(primary_key=True, auto_created=True)
    url = models.CharField(max_length=255)