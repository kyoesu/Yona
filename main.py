from foo import *
from main_chat_foo import *


recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

print("привет! \n я готов!")
voice_input=""
chek=True
while voice_input!="выход" and chek:
# старт записи речи с последующим выводом распознанной речи 
    voice_input = record_and_recognize_audio(recognizer, microphone)
    
    if voice_input=="пока":
        chek=False
    else:
        print(voice_input)


    
    
    
print("пока!!")