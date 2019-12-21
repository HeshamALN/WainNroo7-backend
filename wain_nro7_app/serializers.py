from django.contrib.auth.models import User
from rest_framework import serializers
from wain_nro7_app.models import Place

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    birth_day = serializers.DateField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password', 'gender', 'birth_day' 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        gender = validated_data['gender']
        birth_day= validated_data['birth_day']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name,gender=gender, birth_day=birth_day, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name ", "img", "xcoordinate","ycoordinate", "trivia"]
 





