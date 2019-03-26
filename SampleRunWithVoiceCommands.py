from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import pyaudio
import os

from Display2 import Display2
from Display1 import Display1

root = Tk()

def runProgram2():
    while True:
        y = Display2()
        y.top.update_idletasks()
        y.top.update()
        start_speech_recording()
        #y.top.mainloop()


def runProgram1():
    while True:
        x = Display1()
        x.top.update_idletasks()
        x.top.update()
        start_speech_recording()
        #x.top.mainloop()


LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


def speech_profile_switch():
    global recognised_speech
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Select a user")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:

            recognised_speech = r.recognize_google(audio).lower()
            print("You said: " + r.recognize_google(audio))
            if "display" in recognised_speech:
                runProgram1()

            elif "profile" in recognised_speech:
                runProgram2()

            # elif "Zach" in recognised_speech:
            #     runProgram()
            # elif "Brian" in recognised_speech:
            #     runProgram()
            # elif "Yahye" or "yahaya" in recognised_speech:
            #     runProgram()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def start_speech_recording():
    # Record Audio
    global keyphrase
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            keyphrase = r.recognize_google(audio).lower()
            print("You said: " + r.recognize_google(audio))
            if "smart mirror" in keyphrase:
                #popupmsg("What would you like to do")
                speech_profile_switch()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


#
#
#
# this is the code for the main start screen
#
#
#
# def run_animation():
#     while True:
#         try:
#             global photo
#             global frame
#             global label
#             photo = PhotoImage(
#                 file = photo_path,
#                 format = "gif - {}".format(frame)
#                 )
#
#             label.configure(image = nextframe)
#
#             frame = frame + 1
#
#         except Exception:
#             frame = 1
#             break
#
# photo_path = '/Users/carlt/Desktop/listening.gif'
#
# photo = PhotoImage(
#     file = photo_path,
#     )
# label = Label(
#     image = photo
#     )
# animate = Button(
#     root,
#     text = "animate",
#     command = run_animation
#     )
#
# label.pack()
# animate.pack()



root.title("Welcome to smart mirror")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#feet = StringVar()
#meters = StringVar()

#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Start Voice Commands", command=start_speech_recording).grid(column=3, row=3, sticky=N)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


#feet_entry.focus()
root.bind('<Return>', start_speech_recording)


root.mainloop()


