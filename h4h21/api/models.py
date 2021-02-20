from django.db import models

# Create your models here.
class FoodItem(models.Model):
    poster = models.CharField(max_length=50, unique=False, default="User")
    location = models.CharField(max_length=50, default="Address")
    time_posted = models.DateTimeField(auto_now_add=True)
    time_available = models.DateTimeField(auto_now=False, auto_now_add=False)
    food_name = models.CharField(max_length=20, default="FoodItem")
    food_desc = models.CharField(max_length=50)
    