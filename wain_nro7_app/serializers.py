from django.contrib.auth.models import User
from rest_framework import serializers
from wain_nro7_app.models import Place, Difference, Coordinate#, Profile

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # profile_info = ProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name,gender=gender, birth_day=birth_day, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name", "xcoordinate","ycoordinate", "trivia", "difference", "riddle"]
 
class coorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ["id","xcoordinate","ycoordinate"]
 

class DifferencesSerializer(serializers.ModelSerializer):
    coordinates = coorsSerializer(many=True)
    class Meta:
        model = Difference
        fields = ["id", "diffs", "img", "coordinates"]
 


# class ProfileSerializer(serializers.ModelSerializer):
#     user_info = UserCreateSerializer(many=True)
#     class Meta:
#         model = Profile
#         fields = ['user_info', 'birth_day', 'gander', 'avatar', 'score']



