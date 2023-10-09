from django.db import models

# Create your models here.
class Reg(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField( max_length=100)
    course = models.CharField(max_length=100)
    address = models .CharField(max_length=100)
    