
# Task 3 in DRF registration 

from django.contrib.auth.models import User
from rest_framework import serializers 

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # to hashi the user password and not return with the request 
    class Meta:
        model = User 
        feilds = "username", "password", "first_name", "last_name"

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data
