from .models import Match, Event
from rest_framework import serializers

# source='team2',


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name','coefficient','pk','title']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    team1 = serializers.CharField(source='team1.name',read_only='True')
    team2 = serializers.CharField(source='team2.name',read_only='True')
    sport = serializers.CharField(source='sport.name',read_only='True')
    events = EventSerializer(many=True,read_only=True)

    class Meta:
        model = Match
        fields = ['team1','team2','score','sport','match_id','events']
