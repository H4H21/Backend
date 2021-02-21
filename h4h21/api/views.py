from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from .models import FoodItem
from .serializers import FoodItemSerializer, AddFoodItemSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

import json

# Create your views here.
class FoodItemView(generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

# Add an item to the database
class AddItemView(APIView):
    serializer_class = AddFoodItemSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            poster = self.request.session.session_key
            location = serializer.data.get('location')
            time_available = serializer.data.get('time_available')
            food_name = serializer.data.get('food_name')
            food_cat = serializer.data.get('food_category')
            food_desc = serializer.data.get('food_desc')

            item = FoodItem(poster=poster, location=location, time_available = time_available, food_name = food_name, food_category = food_cat, food_desc=food_desc)
            item.save()
            return Response(FoodItemSerializer(item).data, status=status.HTTP_201_CREATED)
        return Response({"Bad Request" : "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)