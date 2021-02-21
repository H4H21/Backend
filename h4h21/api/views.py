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
from .models import FoodItem
from haversine import haversine, Unit
import re
from requests import Request, post, get
import json

# Create your views here.
class FoodItemView(generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class GetItemView(APIView):
    serializer_class = FoodItemSerializer

    def get(self, request, format=None):
        return(Response({"Get Item View" : "Not implemented yet"}, status=status.HTTP_200_OK))

def convertString(address):
    splitstr = re.split(" |, ", address)
    newstr = splitstr[0]
    for i in range(1, len(splitstr)):
        newstr += "+" + splitstr[i]
    print(address, newstr)
    return newstr

def getDonorLoc(address):
    response = get("https://geocode.search.hereapi.com/v1/geocode?q=" + str(address) + "&apiKey=SRVWUJjjR1Yeiztz_s3jxRVkEVEdbnEC6v4Mr_ktKI0").json()
    print(response)
    response = response['items'][0]
    return response['position']['lat'], response['position']['lng']

def calcDist(r_lat, r_long, d_lat, d_long):
    print(r_lat, r_long, d_lat, d_long)
    return haversine((r_lat, -r_long), (d_lat, d_long), unit="mi")

class GetItemsWithinDist(APIView):
    serializer_class = FoodItemSerializer

    def post(self, request, format=None):
        serializer = FoodItemSerializer(request.data)
        recipient_lat = request.data.get('lat')
        recipient_long = request.data.get('lng')
        limit = request.data.get('dist')

        print(recipient_lat, recipient_long, limit)
        query_set = FoodItem.objects.all().values()

        good = []
        for posting in query_set:
            print("posting:" + str(type(posting)))
            new_string = convertString(posting['location'])
            donor_lat, donor_long = getDonorLoc(new_string)
            
            print(donor_lat, donor_long)
            dist = calcDist(recipient_lat, recipient_long, donor_lat, donor_long)
            print(dist)
            if dist <= limit:
                serializer = self.serializer_class(data=posting)
                if serializer.is_valid():
                    print(type(serializer.data))
                    good.append({'data':serializer.data, 'lat': recipient_lat, 'lng': recipient_long, 'dist': dist})

        for data in good:
            print(data)
        print(json.dumps(good))
        return Response(good, status=status.HTTP_200_OK)
        

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
            time_available_start = serializer.data.get('time_available_start')
            time_available_end = serializer.data.get('time_available_end')
            food_cat = serializer.data.get('food_category')
            if food_cat is None:
                food_cat = ['Other']
            food_desc = serializer.data.get('food_desc')

            item = FoodItem(poster=poster, location=location, time_available_start = time_available_start, time_available_end = time_available_end, food_category = food_cat, food_desc=food_desc)
            item.save()
            return Response(FoodItemSerializer(item).data, status=status.HTTP_201_CREATED)
        return Response({"Bad Request" : "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)