from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from flights.models  import Booking, Flight  
from .serializers import FlightListSerializer,CreateFlightSerilazer 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class ListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = FlightListSerializer 
    permission_classes = [AllowAny]  #any one can access

class CreateView(CreateAPIView):
    serializer_class = CreateFlightSerilazer
    permission_classes = [IsAuthenticated]

class DeleteView(DestroyAPIView):
    queryset = Booking
    serializer_class = FlightListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "object_id"
    permission_classes = [IsAuthenticated,IsAdminUser]
  