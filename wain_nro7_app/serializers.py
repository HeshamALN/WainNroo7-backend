from django.contrib.auth.models import User
from rest_framework import serializers
from wain_nro7_app.models import Place, Difference, Coordinate, Trivia, Question, Answer, Riddle, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user', 'birthday', 'gender', 'total_score']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    birthday = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password', 'email', 'gender', 'birthday']

    def create(self, validated_data):
        print(validated_data)
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        gender = validated_data['gender']
        birthday = validated_data['birthday']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        profile = Profile.objects.create(user=new_user, gender=gender, birthday=birthday, total_score=0)
        return validated_data

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name", "xcoordinate","ycoordinate", "trivia", "difference", "riddle"]
 
class CoorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ["id","xcoordinate","ycoordinate"]
 

class DifferencesSerializer(serializers.ModelSerializer):
    coordinates = CoorsSerializer(many=True)
    class Meta:

        model = Difference
        fields = ["id", "diffs", "img", "coordinates"]
 
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["answer","right","score"]
 
class QuestionsSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True)
    class Meta:
        model = Question
        fields = ["question", "answers"]
 

class TriviaSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)
    class Meta:
        model = Trivia
        fields = ["id", "lock", "questions"]
 

class RiddleSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)
    class Meta:
        model = Riddle
        fields = ["id", "lock", "questions"]
