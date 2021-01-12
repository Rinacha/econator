from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price =  models.IntegerField(blank=True, null=True)
    form = models.TextField()
    mate = models.TextField()
    method = models.TextField()
    color = models.CharField(max_length=100)
    size_d =  models.IntegerField(blank=True, null=True)
    size_w =  models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100)
    pictureURL = models.CharField(max_length=1000)
