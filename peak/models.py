from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Peak(models.Model):
    lat = models.IntegerField(default=1)
    lon = models.IntegerField(default=1)
    altitude = models.IntegerField(default=1)
    name = models.CharField(default='',max_length=100)