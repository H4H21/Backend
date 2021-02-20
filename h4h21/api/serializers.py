from rest_framework import serializers
from .models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('poster', 'location', 'time_posted', 'time_available', 'food_name', 'food_desc')

class AddFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('location', 'time_available', 'food_name', 'food_desc')