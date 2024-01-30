from django.db import models

# Create your models here.

class Buyers(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)