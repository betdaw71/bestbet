from django.db import models
from account.models import User
# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=150,default='Unknown')
    sport_id = models.CharField(max_length=50,default='Unknown')
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=150,default='Unknown')
    def __str__(self):
        return self.name

class Match(models.Model):
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE,related_name='sport')
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team1')
    team2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team2')
    live = models.BooleanField(default=False)
    score = models.CharField(max_length=200,default='0:0')
    match_id = models.CharField(max_length=200,default='0')
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s vs %s'%(self.team1,self.team2)

class Event(models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE,default=1,related_name='events')
    coefficient = models.FloatField(default=1.5)
    name = models.CharField(max_length=150,default='Unknown')
    title = models.CharField(max_length=200,default='Unknown')
    win = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Bet(models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE,default=1,related_name='matchs')
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='bets')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    sum = models.IntegerField()
    coefficient = models.FloatField()
    win = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
class Express(models.Model):
    sum = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usersExpress',default=1)
    win = models.BooleanField(default=False)
    
class BetToExpress(models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE,default=1,related_name='matchsExpress')
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='betsExpress')
    
    coefficient = models.FloatField()
    win = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    express = models.ForeignKey(Express,on_delete=models.CASCADE,related_name='bets')
    

    
