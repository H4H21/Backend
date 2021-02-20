from rest_framework import serializers
from .models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('location', 'time_posted', 'time_available', 'name', 'desc')

class AddFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('location', 'time_available', 'name', 'desc')