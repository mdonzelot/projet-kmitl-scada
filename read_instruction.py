def lire(transcription) :
    global y
    if transcription.count("light")==1 & transcription.count("on")==1 :
        y=1
    if transcription.count("light")==1 & transcription.count("off")==1 :
        y=2
    if transcription.count("brightness")==1 :
        intensite=int(''.join(filter(str.isdigit,transcription)))
        print(intensite)
    if transcription.count("color")==1 :
        if transcription.count("red")==1:
            y=3  
        if transcription.count("blue")==1:
            y=4
        if transcription.count("green")==1:
            y=5
        if transcription.count("white")==1:
            y=6
        else :
            print([int(s) for s in transcription.split() if s.isdigit()])
