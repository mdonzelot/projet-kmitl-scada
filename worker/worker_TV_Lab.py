import redis
import json
import threading
import time
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *
from code_1 import your_custom_storage_is_empty, load_from_your_custom_storage, persist_to_your_custom_storage

#Connexion à la TV
STORE_FILE_PATH = 'store.json'
if your_custom_storage_is_empty():
    store = {}
else:
    store = load_from_your_custom_storage()
client = WebOSClient("192.168.8.126")
client.connect()
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Please accept the connect on the TV!")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful!")
persist_to_your_custom_storage(store)
media = MediaControl(client)
app = ApplicationControl(client)
apps = app.list_apps()
inp = InputControl(client)
system = SystemControl(client)
tv_control = TvControl(client)

# Connexion au serveur Redis
r = redis.Redis(
    host='192.168.8.104',
    port=6379,
    password='ictadmin',
)

pubsub = r.pubsub()

# Souscription au canal spécifique
channel_volume = 'settag2:Room805.LG_TV_Lab.volume'
channel_channel = 'settag2:Room805.LG_TV_Lab.channel'
channel_mute = 'settag2:Room805.LG_TV_Lab.mute'
channel_youtube = 'settag2:Room805.LG_TV_Lab.youtube'
channel_menu = 'settag2:Room805.LG_TV_Lab.menu'
channel_exit = 'settag2:Room805.LG_TV_Lab.exit'
channel_notif = 'settag2:Room805.LG_TV_Lab.notif'
channel_tv='settag2:Room805.LG_TV_Lab.tv'
channel_tvinput = 'settag2:Room805.LG_TV_Lab.channelinput'
channel_program = 'settag2:Room805.LG_TV_Lab.program'
pubsub.subscribe(channel_volume, channel_channel, channel_mute, channel_youtube, channel_menu, channel_exit, channel_notif, channel_tv, channel_tvinput, channel_program)

def handle_tag_volume(message):
    print("tag volume détecté")
    data = message['data'].decode('utf-8')
    json_data = json.loads(data)
    value = json_data.get('value')
    if isinstance(value, str) and value.isdigit():
            value = int(value)
    media.set_volume(value)

def handle_tag_channel(message):
    print("tag channel détecté")
    current_channel = tv_control.get_current_channel()
    channel_number = current_channel.get('channelNumber')
    data = message['data'].decode('utf-8')
    json_data = json.loads(data)
    value = json_data.get('value')
    if value > int(channel_number):
        tv_control.channel_up()
    else : tv_control.channel_down()
    

def handle_tag_mute(message):
    print("tag mute détecté")
    data = message['data'].decode('utf-8')
    json_data = json.loads(data)
    value = json_data.get('value')
    state = True if value == 1 else 0
    media.mute(state)

def handle_tag_youtube(message):
    print("tag youtube détecté")
    yt = [x for x in apps if "youtube" in x["title"].lower()][0]
    app.launch(yt) 
    
def handle_tag_menu(message):
    print("tag menu détecté")
    data = message['data'].decode('utf-8')
    json_data = json.loads(data)
    value = json_data.get('value')
    if value == 1:
        inp.connect_input()
        inp.menu() 
        inp.disconnect_input()

def handle_tag_exit(message):
    print("tag info détecté")
    inp.connect_input()
    inp.exit() 
    inp.disconnect_input()

def handle_tag_notif(message):
    print('tag notif détecté')
    data = message['data'].decode('utf-8')
    json_data = json.loads(data)
    value = json_data.get('value')
    system.notify(value) 

def handle_tag_tv(message):
    print('tag quickChannel détecté')
    tv = [x for x in apps if "live tv" in x["title"].lower()][0]
    app.launch(tv)

def handle_tag_channelinput(message):
    print ('tag channelinput détecté')
    data = message['data'].decode('utf-8')
    json_data = json.loads(data)
    numbers = json_data.get('value')
    inp.connect_input()     
    for number in numbers:
        method_name = f'num_{number}'
        method = getattr(inp, method_name, None)
        method()
    inp.disconnect_input()

def handle_tag_program(message):
    print ('tag program detected')
    inp.connect_input()
    inp.dash()
    inp.disconnect_input()

tag_action = {
    channel_volume: handle_tag_volume,
    channel_channel: handle_tag_channel,
    channel_mute: handle_tag_mute,
    channel_youtube: handle_tag_youtube,
    channel_menu: handle_tag_menu,
    channel_exit: handle_tag_exit,
    channel_notif: handle_tag_notif,
    channel_tv: handle_tag_tv,
    channel_tvinput : handle_tag_channelinput,
    channel_program: handle_tag_program
}

print("Waiting for tag...")

def listen_scada():
    for message in pubsub.listen():
        print(f"Message received: {message}")
        if message['type'] == 'message':
            tag = message['channel'].decode('utf-8')
            data = message['data'].decode('utf-8')
            
            print(f"Tag: {tag}, Data: {data}")
            
            if tag in tag_action:
                tag_action[tag](message)
            
def update_status_scada():
    while True:
        print('Updtating data in Scada...')
        try:
            current_channel = tv_control.get_current_channel()
            channel_number = current_channel.get('channelNumber')
            r.set('tag:Room805.LG_TV_Lab.channel', channel_number)
        except Exception as e:
                print(f"Erreur lors de la récupération du canal: {e}")
        
        volume_status = media.get_volume()
        volume = volume_status.get('volume')
        mute = 1 if volume_status.get('muted') else 0
        r.set('tag:Room805.LG_TV_Lab.volume', volume)
        r.set('tag:Room805.LG_TV_Lab.mute', mute)
        
        time.sleep(5)


listener_thread = threading.Thread(target=listen_scada)
updater_thread = threading.Thread(target=update_status_scada)

listener_thread.start()
updater_thread.start()

listener_thread.join()
updater_thread.join()