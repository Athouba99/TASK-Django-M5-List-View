from rest_framework.generics import FlightAPIView
from .models import Booking, Flight
from .serializers import FlightsSerializer
class Flights(FlightAPIView):
   id = Flight.objects.all(id=id)
   destination = Flight.objects.all()
   time = Flight.objects.all()
   price = Flight.objects.all()

