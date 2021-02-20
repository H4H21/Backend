from django.db import models

# Create your models here.
class FoodItem(models.Model):
    poster= = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    time_posted = models.DateTimeField(auto_now_add=True)
    time_available = models.DateTimeField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    