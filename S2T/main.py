import speech_recognition as sr
import os
from openai import OpenAI
from light_function import turn_light_onoff, switch_light_birghtness, switch_light_color
from tv_function import turn_tv_onoff, turn_tv_mute, switch_tv_volume, switch_tv_channel


openai_client = OpenAI()

record = sr.Recognizer()
with sr.Microphone() as source:
    record.adjust_for_ambient_noise(source)
    print("Say something !")
    try:
        audio = record.listen(source, phrase_time_limit=5)
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
    
folder = "./Audio"
filename = "instruction_audio"
audio_file_path = f"{folder}/{filename}.wav"

if not os.path.exists(folder):
    os.mkdir(folder)

print(f"Generating WAV file, saving at location: {audio_file_path}")
with open(audio_file_path,"wb") as f:
    f.write(audio.get_wav_data())

audio_file = open("C:/Users/maxim/Documents/KMITL/Work/Code/Audio/instruction_audio.wav","rb")

translation = openai_client.audio.translations.create(
        model='whisper-1',
        file=audio_file
    )
print(translation.text)

translation_text = translation.text.lower()  # Convertir le texte traduit en minuscules pour une comparaison sans casse
if translation_text.count("alpha"):
     lightNbr = 1
elif translation_text.count("beta"):
     lightNbr = 2
elif translation_text.count("omega"):
     lightNbr = 3
if translation_text.count("light") == 1 and translation_text.count("on") == 1:
    turn_light_onoff(1, 1)
elif translation_text.count("light") == 1 and translation_text.count("off") == 1:
    turn_light_onoff(0, lightNbr)
elif translation_text.count("brightness") == 1:
    intensite = int(''.join(filter(str.isdigit, translation_text)))
    switch_light_birghtness(intensite, lightNbr)
elif translation_text.count("color")==1 :
        if translation_text.count("red")==1:
            color="#FF0000"  
            switch_light_color(color, lightNbr)
        if translation_text.count("blue")==1:
            color="#0000FF"
            switch_light_color(color, lightNbr)
        if translation_text.count("green")==1:
            color="#00FF00"
            switch_light_color(color, lightNbr)
        if translation_text.count("white")==1:
            color="#FFFFFF"
            switch_light_color(color, lightNbr)

elif translation_text.count("turn on")==1 & translation_text.count("tv")==1:
        turn_tv_onoff(1)
elif translation_text.count("turn off")==1 & translation_text.count("tv")==1:
        turn_tv_onoff(0)
elif translation_text.count("unmute")==1 & translation_text.count("tv")==1:
        turn_tv_mute(0)
elif translation_text.count("mute")==1 & translation_text.count("tv")==1:
        turn_tv_mute(1)
elif translation_text.count("channel")==1 :
        channel=int(''.join(filter(str.isdigit,translation_text)))
        switch_tv_channel(channel)
elif translation_text.count("volume")==1 :
        volume=int(''.join(filter(str.isdigit,translation_text)))
        switch_tv_volume(volume)
