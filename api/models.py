from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    mobile = models.IntegerField()
    imgUri = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
