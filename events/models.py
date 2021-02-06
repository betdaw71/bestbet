from django.db import models
from account.models import User
# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=150,default='Unknown')
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=150,default='Unknown')
    def __str__(self):
        return self.name

class Match(models.Model):
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team1')
    team2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team2')
    live = models.BooleanField(default=False)

    def __str__(self):
        return '%s vs %s'%(self.team1,self.team2)

class Event(models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE,default=1,related_name='events')
    coefficient = models.FloatField(default=1.5)
    name = models.CharField(max_length=150,default='Unknown')
    def __str__(self):
        return self.name

class Bet(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='bets')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    sum = models.IntegerField()
    coefficient = models.FloatField()
