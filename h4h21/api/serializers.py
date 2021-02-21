from rest_framework import serializers
from .models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('poster', 'location', 'time_posted', 'time_available_start', 'time_available_end', 'food_category', 'food_desc')

class AddFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('location', 'time_available_start', 'time_available_end', 'food_category', 'food_desc')