from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, PlacesSerializer, DifferencesSerializer, TriviaSerializer#, ProfileSerializer
from .models import Place, Difference, Trivia#, Profile
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView
	)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# Create your views here.
class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	permission_classes = [AllowAny]

class MapListView(ListAPIView):
	queryset = Place.objects.all()
	serializer_class = PlacesSerializer
	permission_classes = [AllowAny]

class DiffView(RetrieveAPIView):
	queryset = Difference.objects.all()
	serializer_class = DifferencesSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'diff_id'
	permission_classes = [AllowAny]

class TriviaView(RetrieveAPIView):
	queryset = Trivia.objects.all()
	serializer_class = TriviaSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'trivia_id'
	permission_classes = [AllowAny]

# class ProfileAPIView(RetrieveAPIView):
# 	serializer_class = ProfileSerializer
# 	permission_classes = [IsAuthenticated]

# 	def get_object(self):
# 		return self.request.user

# class Score(APIView):

# 	permission_classes= [IsAuthenticated]

# 	def post(self, request, format=None):
# 		profile = request.user.profile
# 		profile.score += request.POST.get('score')
# 		profile.save()
# 		return Response()

