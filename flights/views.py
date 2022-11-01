#in DRF the views are class based
from datetime import date
from pytz import timezone
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Booking, Flight
from flights.serializers import FlightListSerializer,BookingListSerializer, BookingDetalListSerializer 
from django.utils import timezone

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
