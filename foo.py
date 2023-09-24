def bot_mod (ask):
    que="Yona say: "

    #обработка запроса
    que+=ask
    
    
    return que
def bot (ask):
    if ask=="error":
        return "error 404!!!"
    else:
        return bot_mod(ask) 



import speech_recognition
def record_and_recognize_audio(recognizer, microphone):
    
    #Запись и распознавание аудио
    
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Слушаю")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google 
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data