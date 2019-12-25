from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Place(models.Model):
    name = models.CharField(max_length=120)
    # location = 
    # lock = models.BooleanField(default= False)
    xcoordinate= models.FloatField()
    ycoordinate= models.FloatField()
    def __str__(self):
        return self.name

class Trivia(models.Model):
    lock=models.BooleanField(default= False)
    place= models.OneToOneField(Place, on_delete=models.CASCADE, related_name="trivia" )
    # profile=models.ManyToManyField(Profile, related_name="trivias" )
    # score=models.FloatField()
    def __str__(self):
        return self.place.name

class Questions(models.Model):
    question=models.TextField()
    # order=models.PositiveIntegerField()
    trivia=models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name="questions" )
    def __str__(self):
        return self.question

class Answers(models.Model):
    answer=models.TextField()
    right=models.BooleanField(default= False)
    score=models.FloatField()
    questions= models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers" )
    def __str__(self):
        return self.questions.question


class Difference(models.Model):
    place=  models.OneToOneField(Place, on_delete=models.CASCADE, related_name="difference" )
    img=models.ImageField(upload_to='', null=True, blank=True)
    diffs=models.PositiveIntegerField()
    def __str__(self):
        return self.place.name

class Coordinate(models.Model):
    xcoordinate=models.FloatField()
    ycoordinate=models.FloatField()
    difference=models.ForeignKey(Difference, on_delete=models.CASCADE, related_name="coordinates" )

class Riddle(models.Model):
    place=  models.OneToOneField(Place, on_delete=models.CASCADE, related_name="riddle" )
    def __str__(self):
        return self.place.name

# class Profile(models.Model):
#     Male = 'Male'
#     Female = 'Female'
#     GENDER = [
#     ('Male','Male'),
#     ('Female', 'Female')]

#     birthday=models.DateField()
#     gender=models.CharField(choices=GENDER, max_length=6)
#     avatar=models.ImageField(upload_to='', null=True, blank=True)
#     score= models.PositiveIntegerField()
#     user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile" )

# class Games(models.Model):
#   trivia= models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name="Trivia" )
#   riddle= models.ForeignKey(Riddles, on_delete=models.CASCADE, related_name="Riddles" )
#   difference= models.ForeignKey(Diff, on_delete=models.CASCADE, related_name="Diff" )