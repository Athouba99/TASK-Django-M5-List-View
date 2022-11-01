
# Task 3 in DRF registration
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import RegisterSerializer

# Create your views here.
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    