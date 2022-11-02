#in DRF the views are class based
from datetime import date
from pytz import timezone
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Booking, Flight
from flights.serializers import FlightListSerializer,BookingListSerializer, BookingDetalListSerializer 
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializers import FlightListSerializer,RegisterSerializer,LoginSerializer,CreateFlightSerilazer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
# Task 3 in DRF registration

from django.shortcuts import render
from rest_framework.generics import CreateAPIView


# Task 4 in DRF Create & login view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class FlightListView(ListAPIView): #1rt view
    queryset = Flight.objects.all()#fetch all the flight instances
    serializer_class = FlightListSerializer 

class NextBookingListView(ListAPIView): #2nd vieew 
    queryset = Flight.objects.all() #to fetch 
    serializer_class = BookingListSerializer
    
class BookingListView(ListAPIView): #3rd view 
    queryset = Booking.objects.filter(date__gt=timezone.now()) # filter the fetching only for upcoming boking by date, not for all the fields
    serializer_class = BookingListSerializer # user the same serializer as 2nd view, using the same field to display 

# Task 2
class BookingDetailListView(RetrieveAPIView):#4th view
    queryset = Booking.objects.all()
    serializer_class = BookingDetalListSerializer 
    lookup_field = "id" #identifying the objects
    lookup_url_kwarg = "object_id"


class BookingUpdateListView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetalListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "object_id"


class DeleteBookingListView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListView
    lookup_field = "id"
    lookup_url_kwarg = "object_id"

# Task 3 register
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

#Task 4 create & login 
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# Task 5 

class CreateFlight(CreateAPIView):
     queryset = Booking.objects.all()
     serializer_class = CreateFlightSerilazer
     permission_classes = [IsAuthenticated]



