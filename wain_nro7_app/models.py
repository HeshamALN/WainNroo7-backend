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
    img = models.ImageField(upload_to='', null=True, blank=True)
    xcoordinate= models.FloatField()
    ycoordinate= models.FloatField()
    # trivia= models.OneToOneField(Trivia, on_delete=models.CASCADE, related_name="Trivia" )
    # riddle= models.ForeignKey(Riddles, on_delete=models.CASCADE, related_name="Riddles" )
    # diff= models.ForeignKey(Diff, on_delete=models.CASCADE, related_name="Diff" )
    def __str__(self):
        return self.name



class Trivia(models.Model):
    # qustions= models.ForeignKey(Qustion, on_delete=models.CASCADE, related_name="qustion" )
    # lock=models.BooleanField(default= False)
    # score=models.FloatField()
    place= models.OneToOneField(Place, on_delete=models.CASCADE, related_name="Place" )
    profile=models.ManyToManyField(Profile, related_name="trivias" )


class Question(models.Model):
    question=models.TextField()
    order=models.PositiveIntegerField()
    trivia=models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name="questions" )
    #


class Answer(models.Model):
    answers=models.TextField()
    correct=models.BooleanField(default= False)
    questions= models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers" )



class Profile(models.Model):
    birth_day=models.DateField()
    gander=models.IntegerField(choices=((1, ("Male")),
                                        (2, ("Female"))),
                                default=1)
    avatar=models.ImageField(upload_to='', null=True, blank=True)
    score= models.PositiveIntegerField()
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile" )




class Diff(models.Model):
    img=models.ImageField(upload_to='', null=True, blank=True)
    coordinate=models.ForeignKey(Coordinate, on_delete=models.CASCADE, related_name="coordinate" )




class Coordinate(models.Model):
  xcoordinate=models.FloatField()
  ycoordinate=models.FloatField()





# class Games(models.Model):
#   trivia= models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name="Trivia" )
#   riddle= models.ForeignKey(Riddles, on_delete=models.CASCADE, related_name="Riddles" )
#   diff= models.ForeignKey(Diff, on_delete=models.CASCADE, related_name="Diff" )



