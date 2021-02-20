from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from .models import FoodItem
from .serializers import FoodItemSerializer, AddFoodItemSerializer
from rest_framework.views import APIView
from rest_framework import generics

import json

# Create your views here.
class FoodItemView(generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class AddItemView(APIView):
    serializer_class = AddFoodItemSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
