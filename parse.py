import websocket
import threading
import time

def on_message(ws, message):
    time.sleep(1)
    if message.split(',')[1].replace('"','') == 'update_markets':
        # time.sleep(3)
        for i in message.split('[[')[1].split('],['):
            print('Market  - ',message.split(',')[2].replace('"',''),'   -     ',i.split(',')[0].replace('"',''),i.split(',')[2].replace('"',''),i.split(',')[8].replace('"','').split('name')[1].replace('\\:\\','').replace('\\','  '))
    if message.split(',')[1].replace('"','') == 'update_event':
        print('Event  - ',message.split(',')[2].replace('"', ''),'   -    ',message.split(',')[7].split(':')[1].replace('"',''),message.split(',')[8].split(':')[1].replace('"',''),message.split(',')[9].split(':')[1].replace('"',''),message.split(',')[10].split(':')[1].replace('"',''),message.split(',')[11].split(':')[1].replace('"',''),message.split(',')[12].split(':')[1].replace('"',''),message.split(',')[15].split('":"')[1].replace('"',''))

def on_error(ws, error):
    print (error)

def on_close(ws):
    print( "### closed ###")

def on_open(ws):
    ws.send('{"cmd": "subscribe", "auth_key":"315e44244fd8c4fb4e24c2786d3d8cc6", "needed_bk":["bet365:live"]}')



if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://api.oddscp.com:8001",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()
