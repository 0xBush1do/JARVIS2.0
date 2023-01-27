from vocalFunc import *
from chatGPT import *
import time, threading, concurrent.futures
from utility import *

if __name__ == "__main__":
    speak("Ciao! Sono Jarvis il tuo assistente vocale")
    while True:
        speak("Chiedimi pure ciò che vuoi!")
        command = listen()
        while command == '':
            command = listen()
        if "stop" in command:
            speak("Grazie per aver parlato con me! Alla prossima!")
            break
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(askGPT, command)
        speak(loadingSentences())
        speak(future.result())
        time.sleep(3)
        speak("Se hai bisogno di altro, basta chiedere! altrimenti pronuncia la parola 'stop' per terminare la comunicazione")