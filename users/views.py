
# Task 3 in DRF registration
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import RegisterSerializer

# Create your views here, it is class based view
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
