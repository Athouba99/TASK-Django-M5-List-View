

from django.contrib.auth.models import User
from rest_framework import serializers 


# Task 3 in DRF registration 
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

# Task 4 : create & login view
class LoginSerializer(serializers.Serializer): # no modelserializer to login because login don't make objs 
    username = serializers.CharField()
    password = serializers.CharField(wirte_only=True) # write only passed to the attribute to hash the password

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise serializers.ValidationError("This username doesn't exist")

    if not user.check_password(password):
        '''
        return data #[check which lib its from ]
          '''
    else:
        raise serializers.ValidationError("Incorrect username or password ")
