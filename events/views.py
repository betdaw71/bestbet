from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from account.models import User
from django.contrib import messages
from rest_framework import viewsets
from .serializers import MatchSerializer,EventSerializer
from rest_framework import permissions
from rest_framework import generics

# Create your views here.

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        ido = self.kwargs['sport']
        return Match.objects.filter(sport=Sport.objects.get(name=ido))
    
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        id = self.kwargs['match_id']
        return Event.objects.filter(match=Match.objects.get(match_id=id))


def list(request,sport='soccer'):
    events = Match.objects.all()
    sports = Sport.objects.all()
    
    data={
        'events' : events,
        'sports' : sports,
        'sport':Sport.objects.get(name=sport),
    }
    return render(request, 'events/list.html',context=data)

def match(request,sport,match_id):
    match = Match.objects.get(match_id=match_id)
    data = {
        'match' : match
    }
    return render(request,'events/match.html',context=data)

def event(request,sport,match_id,event):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        if user.balance >= int(request.POST.get('sum')):
            eventD = Event.objects.get(id=event)
            match = Match.objects.get(match_id=match_id)
            bet = Bet.objects.create(event=eventD,match=match,user=user, sum=int(request.POST.get('sum')), coefficient=eventD.coefficient)
            user.balance -= int(request.POST.get('sum'))
            user.save()
            return render(request,'events/sucsess.html')
        else:
            messages.error(request,'Недостаточно средств')
    else:
        pass
    data = {
        'sport':sport,
        'match_id':match_id,
        'event':event,
    }
    return render(request,'events/event.html',context=data)


def express(request,sport,match_id,event):
    user = User.objects.get(id=request.user.id)
    express = Express.objects.filter(user=user)
    data={
        'express':express,
    }
    return render(request,'events/express_all.html',context=data)

def express_add(request):
    return render(request,'events/express_add.html')
