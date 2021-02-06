from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from account.models import User
from django.contrib import messages

# Create your views here.

def list(request):
    events = Match.objects.all()
    data={
        'events' : events
    }
    return render(request, 'events/list.html',context=data)

def match(request,pk):
    match = Match.objects.get(pk=pk)
    data = {
        'match' : match
    }
    return render(request,'events/match.html',context=data)

def event(request,match,event):
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
