from django.db import models

# Create your models here.

class Measurement(models.Model):
    Temperature = models.FloatField(max_length=100)
    Humidity = models.FloatField(max_length=100)