from dataclasses import field
from .models import Booking, Flight
from rest_framework.generics import serializers
from .serializers import FlightsSerializer

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight 
        fields = ["id","destination","time","price"]
         
