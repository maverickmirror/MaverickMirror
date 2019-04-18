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

# root = Tk()

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

#
def runAnimation():
    while True:
        p = DisplayAnimation()
        #g = multiprocessing.Process(target=speech_profile_switch, name='speechrecording')
        #g.start()
        p.top.mainloop()


def runProgram1():
    while True:
        x = Display1()
        #t = multiprocessing.Process(target=start_speech_recording, name='speechrecording2')
        #t.start()
        x.top.mainloop()
#
#
def runProgram2():
    while True:
        y = Display2()
        #u = multiprocessing.Process(target=start_speech_recording, name='speechrecording3')
        #u.start()
        y.top.mainloop()


def start_speech_recording(q):
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
                q.put('run animation')


        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def speech_profile_switch(q):
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
                q.put('display1')

            elif "profile" in recognised_speech:
                q.put('display2')

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



# def program2(keyword):
#     if keyword == 'display1':
#         display1 = multiprocessing.Process(target=runProgram1)
#         display1.start()
#         voice1 = multiprocessing.Process(target=start_speech_recording, args=(q,))
#         voice1.start()
#         keyword2 = q.get()
#         voice1.terminate()
#         program(keyword2)
#
#     elif keyword == 'display2':
#         display2 = multiprocessing.Process(target=runProgram2)
#         display2.start()
#         voice2 = multiprocessing.Process(target=start_speech_recording, args=(q,))
#         voice2.start()
#         keyword2 = q.get()
#         voice2.terminate()
#         program(keyword2)

def program():
        k = ''
        animation = multiprocessing.Process(target=runAnimation, name='animation')
        animation.start()
        profile = multiprocessing.Process(target=speech_profile_switch, args=(q,))
        profile.start()
        newkeyword = q.get()
        profile.terminate()

        if newkeyword == 'display1':
            animation.terminate()

            display1 = multiprocessing.Process(target=runProgram1)
            display1.start()
            voice1 = multiprocessing.Process(target=start_speech_recording, args=(q,))
            voice1.start()
            keyword2 = q.get()
            if keyword2 == 'run animation':
                voice1.terminate()
                program()

        elif newkeyword == 'display2':
            animation.terminate()
            display2 = multiprocessing.Process(target=runProgram2)
            display2.start()
            voice2 = multiprocessing.Process(target=start_speech_recording, args=(q,))
            voice2.start()
            keyword2 = q.get()
            if keyword2 == 'run animation':
                voice2.terminate()
                program()


if __name__ == '__main__':
    try:
        multiprocessing.set_start_method('spawn')
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=start_speech_recording, args=(q,))
        startup = multiprocessing.Process(target=runProgramStart, name='startup')
        startup.start()
        p.start()
        #print(q.get())
        keyword = q.get()
        if keyword == 'run animation':
            p.terminate()
            program()



    except Exception as e:
        print("Error: unable to start thread")
        print(e)

    while 1:
        pass

# if __name__ == '__main__':
#     ctx = multiprocessing.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=start_speech_recording, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()
    # try:
    #
    #     startscreen = multiprocessing.Process(target=runProgramStart, name='startscreen')
    #     startscreen.start()
    #     speechrecording = multiprocessing.Process(target=start_speech_recording, name='speechrecording')
    #     speechrecording.start()
    #
    # except Exception as e:
    #     print("Error: unable to start thread")
    #     print(e)
    #
    # while 1:
    #     pass


