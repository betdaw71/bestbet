import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bet.settings")

import django
django.setup()

from django.core.management import call_command

import websocket
import threading
import time
from events.models import *

def on_message(ws, message):
    # time.sleep(1)
    print(message)
    if message.split(',')[1].replace('"','') == 'update_markets':
        # time.sleep(3)
        for i in message.split('[[')[1].split('],['):
            id = message.split(',')[2].replace('"','')
            name = i.split(',')[0].replace('"','')
            coefficient = i.split(',')[2].replace('"','')
            title = i.split(',')[8].replace('"','').split('name')[1].replace('\\:\\','').replace('\\','  ')

            try:
                match = Match.objects.get(match_id=id)
                try:
                    event = match.events.all.get(name=name)
                    event.coefficient = float(coefficient)
                    event.save()
                    print('Event have been updated')
                except:
                    event = Event.objects.create(match=match,coefficient=float(coefficient),name=name,title=title)
                    print('Event have been created')
            except:
                print('Match does not exist')
            print('Market  - ',id,'   -     ',name,coefficient,title)
    if message.split(',')[1].replace('"','') == 'update_event':
        id = message.split(',')[2].replace('"', '')
        sport_id = message.split(',')[7].split(':')[1].replace('"','')
        sport_name = message.split(',')[8].split(':')[1].replace('"','')
        match_name = message.split(',')[9].split(':')[1].replace('"','')
        team1 = message.split(',')[10].split(':')[1].replace('"','')
        team2 = message.split(',')[11].split(':')[1].replace('"','')
        league = message.split(',')[12].split(':')[1].replace('"','')
        score =message.split(',')[15].split('":"')[1].replace('"','')

        try:
            sport = Sport.objects.get(sport_id=sport_id)
        except:
            sport = Sport.objects.create(name=sport_name,sport_id=sport_id)

        try:
            team_one = Team.objects.get(name=team1)
        except:
            team_one = Team.objects.create(name=team1)

        try:
            team_two = Team.objects.get(name=team2)
        except:
            team_two = Team.objects.create(name=team2)

        try:
            match = Match.objects.get(match_id=id)
            if match.score != score:
                match.score = score
                match.save()
                print('Update To',score)
            else:
                print('Nothing To Update')
        except:
            match = Match.objects.create(sport=sport,team1=team_one,team2=team_two,score=score,match_id=id)
            print('Sucsesfully Added')
        # print('Event  - ',id,'   -    ',sport_id,'  ,  ',sport_name,'  ,  ',match_name,'  ,  ',team1,'  ,  ',team2,'  ,  ',league,'  ,  ',score)

def on_error(ws, error):
    print (error)

def on_close(ws):
    print( "### closed ###")

def on_open(ws):
    ws.send('{"cmd": "subscribe", "auth_key":"315e44244fd8c4fb4e24c2786d3d8cc6", "needed_bk":["bet365:live"]}')



def main():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://api.oddscp.com:8001",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

if __name__ == '__main__':
    main()
