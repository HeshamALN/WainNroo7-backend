from django.shortcuts import render
from django.contrib.auth.models import User,
from serializers import UserCreateSerializer,

# Create your views here.
 class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

	