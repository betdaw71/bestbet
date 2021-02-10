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

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        id = self.kwargs['match_id']
        return Event.objects.filter(match=Match.objects.get(match_id=id))


def list(request):
    events = Match.objects.all()
    data={
        'events' : events
    }
    return render(request, 'events/list.html',context=data)

def match(request,match_id):
    match = Match.objects.get(match_id=match_id)
    data = {
        'match' : match
    }
    return render(request,'events/match.html',context=data)

def event(request,match_id,event):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        if user.balance >= int(request.POST.get('sum')):
            eventD = Event.objects.get(id=event)
            bet = Bet.objects.create(event=eventD,user=user, sum=int(request.POST.get('sum')), coefficient=eventD.coefficient)
            user.balance -= int(request.POST.get('sum'))
            user.save()
            return render(request,'events/sucsess.html')
        else:
            messages.error(request,'Недостаточно средств')
    else:
        pass
    return render(request,'events/event.html')
