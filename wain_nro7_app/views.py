from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, PlacesSerializer, ProfileSerializer
from .models import Place, Profile
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView
	)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# Create your views here.
class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	permission_classes = [AllowAny]

class MapListView(ListAPIView):
	queryset = Place.objects.all()
	serializer_class = PlacesSerializer
	permission_classes = [AllowAny]

class ProfileAPIView(RetrieveAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user
