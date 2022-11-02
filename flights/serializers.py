from pyexpat import model
from rest_framework import serializers
from .models import Booking, Flight
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from flights.models import Flight, Booking
from rest_framework_simplejwt.tokens import RefreshToken
# in DRF place the models in this file 
User = get_user_model()



# Task 1 
class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight 
        fields = ["id","destination","time","price"]

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight","date","id"]

# Task 2 
class BookingDetalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        feilds = ["id","flight","date","passengers"]


class BookingUpdateListView(serializers.ModelSerializer):
    class Meta:
        model = Booking
        feilds = ["date","passengers"]

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
    token = serializers.CharField(read_only=True, allow_blanck=True) #token has another name which is access
    def validate(self, data):

        username = data.get("username")
        password = data.get("password")

        #got the above lines from warehouse 'Generating A Token' 

        try:
           user = User.objects.get(username=username)
        except User.DoesNotExist:
           raise serializers.ValidationError("This username doesn't exist")

        if  user.check_password(password):
            payload = RefreshToken.for_user(user) #[user is being underlined are error]
            token = str(payload.access_token) #[paylod is being underlined are error]
            raise serializers.ValidationError("Incorrect username or password ") 
            data["access"] = token
            return data #[check which lib its from, it's not a lib ]

        else: 
            raise serializers.ValidationError("incoreect username or password")
       



# Task 5 
class CreateFlightSerilazer(serializers.ModelSerializer):
    passengers = serializers.PrimaryKeyRelatedField(read_only=True) #
    class Meta:
        model = Booking
        fields = ["id","date","flight", "passengers"]

