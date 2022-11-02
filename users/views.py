
# Task 3 in DRF registration

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import RegisterSerializer

# Task 4 in DRF Create & login view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializer import LoginSerializer

# Create your views here, it is class based view

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

