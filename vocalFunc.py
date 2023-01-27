from gtts import gTTS
import speech_recognition as sr, os, time, playsound

def speak(text):
    filename = f"{int(time.time())}.mp3"

    # creating TTS object
    tts = gTTS(text=text, lang='it')

    # saving mp3 file
    tts.save(filename)

    # playing mp3 file
    playsound.playsound(filename, True)

    # removing mp3 file
    os.remove(filename)

def listen():
    # creating recognizer object
    r = sr.Recognizer()

    # setting microphone as input
    with sr.Microphone() as source:
        audio = r.listen(source)

    # recognizing command
    try:
        command = r.recognize_google(audio, language='it-IT')
        print(f"Hai detto: {command}")

    except sr.UnknownValueError:
        #speak("Non sono riuscito a capire cosa hai detto")
        return ''
    except sr.RequestError as e:
        print("Errore di richiesta; {0}".format(e))
    return command