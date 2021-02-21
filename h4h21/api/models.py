from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class FoodItem(models.Model):
    poster = models.CharField(max_length=50, unique=False, default="User")
    location = models.CharField(max_length=50, default="Address")
    time_posted = models.DateTimeField(auto_now_add=True)
    time_available = models.DateTimeField(auto_now=False, auto_now_add=False)
    food_name = models.CharField(max_length=20, default="FoodItem")
    foodslist = ArrayField(
        models.CharField(max_length=15),
        size = 4
    )
    food_category = models.CharField(max_length=50, default="Category")
    food_desc = models.CharField(max_length=50)
    