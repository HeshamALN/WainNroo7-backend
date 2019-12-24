from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=120)
    # location = 
    # lock = models.BooleanField(default= False)
    xcoordinate= models.FloatField()
    ycoordinate= models.FloatField()
    def __str__(self):
        return self.name



class Trivia(models.Model):
    # qustions= models.ForeignKey(Qustion, on_delete=models.CASCADE, related_name="qustion" )
    # lock=models.BooleanField(default= False)
    # score=models.FloatField()
    place= models.OneToOneField(Place, on_delete=models.CASCADE, related_name="trivia" )
    # profile=models.ManyToManyField(Profile, related_name="trivias" )


class Question(models.Model):
    question=models.TextField()
    order=models.PositiveIntegerField()
    trivia=models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name="questions" )


class Answer(models.Model):
    answers=models.TextField()
    correct=models.BooleanField(default= False)
    questions= models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers" )


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


class Difference(models.Model):
    place=  models.OneToOneField(Place, on_delete=models.CASCADE, related_name="difference" )
    img=models.ImageField(upload_to='', null=True, blank=True)
    diffs=models.PositiveIntegerField()


class Coordinate(models.Model):
    xcoordinate=models.FloatField()
    ycoordinate=models.FloatField()
    difference=models.ForeignKey(Difference, on_delete=models.CASCADE, related_name="coordinates" )

class Riddle(models.Model):
    place=  models.OneToOneField(Place, on_delete=models.CASCADE, related_name="riddle" )
    

# class Games(models.Model):
#   trivia= models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name="Trivia" )
#   riddle= models.ForeignKey(Riddles, on_delete=models.CASCADE, related_name="Riddles" )
#   difference= models.ForeignKey(Diff, on_delete=models.CASCADE, related_name="Diff" )



