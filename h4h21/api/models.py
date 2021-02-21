from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class FoodItem(models.Model):
    poster = models.CharField(max_length=50, unique=False, default="User")
    location = models.CharField(max_length=50, default="Address")
    time_posted = models.DateTimeField(auto_now_add=True)
    time_available_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    time_available_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    food_category = ArrayField(base_field=models.CharField(max_length=15, unique=False, blank=True), size=5, default=list)
    food_desc = models.CharField(max_length=50)
    