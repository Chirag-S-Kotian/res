from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    items = models.TextField()
    lat_long = models.CharField(max_length=100)
    full_details = models.TextField()
    
    def __str__(self):
        return self.name
