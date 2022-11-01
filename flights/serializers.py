from pyexpat import model
from rest_framework import serializers
from .models import Booking, Flight

# in DRF place the models in this file 

# Task 1 
class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight 
        fields = ["id","destination","time","price"]

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight","date","id"]

# Task 2 
class BookingDetalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        feilds = ["id","flight","date","passengers"]


class BookingUpdateListView(serializers.ModelSerializer):
    class Meta:
        model = Booking
        feilds = ["date","passengers"]


