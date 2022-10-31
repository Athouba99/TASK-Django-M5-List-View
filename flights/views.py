#in DRF the views are class based
from pytz import timezone
from rest_framework.generics import ListAPIView
from .models import Booking, Flight
from flights.serializers import FlightListSerializer,BookingListSerializer 
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

