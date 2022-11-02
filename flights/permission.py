from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from flights.models  import Booking, Flight  
from .serializers import FlightListSerializer 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class ListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = FlightListSerializer 
    permission_classes = [AllowAny]  #any one can access

class CreateView(CreateAPIView):
    serializer_class = 
