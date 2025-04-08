from django.db import models
import os

# Create your models here.
class Form(models.Model):  
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    course = models.CharField( max_length=50)
    def __str__(self):
        return f"{self.name}"

