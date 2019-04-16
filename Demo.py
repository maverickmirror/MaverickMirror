from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import pyaudio
import os
import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as mp
import pandas as pd
import pandas_datareader.data as wb
import multiprocessing
import locale
import threading


from Display2 import Display2
from Display1 import Display1
from DisplayStart import DisplayStart
from DisplayAnimation import DisplayAnimation

LOCALE_LOCK = threading.Lock()
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

root = Tk()




def setlocale(name): #thread proof function to work with locale
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

def runProgramStart():
    while True:
        b = DisplayStart()
        b.tk.mainloop()


def runAnimation():
    while True:
        p = DisplayAnimation()
        g = multiprocessing.Process(target=speech_profile_switch, name='speechrecording')
        g.start()
        p.top.mainloop()


def runProgram1():
    while True:
        x = Display1()
        t = multiprocessing.Process(target=start_speech_recording, name='speechrecording2')
        t.start()
        x.top.mainloop()


def runProgram2():
    while True:
        y = Display2()
        u = multiprocessing.Process(target=start_speech_recording, name='speechrecording3')
        u.start()
        y.top.mainloop()


def start_speech_recording():
    global keyphrase
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source, duration=.5)
            audio = r.listen(source)

        try:
            keyphrase = r.recognize_google(audio).lower()
            print("You said: " + r.recognize_google(audio))
            if "hello" in keyphrase:
                return runAnimation()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



def speech_profile_switch():
    global recognised_speech
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Select a user")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        try:
            recognised_speech = r.recognize_google(audio).lower()
            print("You said: " + r.recognize_google(audio))
            if "home" in recognised_speech:
                return runProgram1()

            elif "profile" in recognised_speech:
                return runProgram2()

            elif "cancel" in recognised_speech:
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == '__main__':

    try:

        startscreen = multiprocessing.Process(target=runProgramStart, name='startscreen')
        startscreen.start()
        speechrecording = multiprocessing.Process(target=start_speech_recording, name='speechrecording')
        speechrecording.start()

    except Exception as e:
        print("Error: unable to start thread")
        print(e)

    while 1:
        pass


