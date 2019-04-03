from tkinter import *
from tkinter import ttk
import time
import requests
import json
import traceback
import feedparser
import schedule
import speech_recognition as sr
import pyaudio

xLargeText = 80
largeText = 56
mediumText = 28
smallText = 15


class Message(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        self.messageLabel = Label(self, text="Welcome to Smart Mirror", font=("Verdana", mediumText), fg="white",
                                  bg="black")
        # sets location on screen and orientation
        self.messageLabel.pack(side=TOP, anchor=N)
        self.messageLabel2 = Label(self, text="Say 'Hello' to begin", font=("Verdana", smallText), fg="white",
                                  bg="black")
        # sets location on screen and orientation
        self.messageLabel2.pack(side=TOP, anchor=N)

    #     self.photo = PhotoImage(file="listening.gif")
    #     frame1 = PhotoImage(file='listening.gif', format="gif -index 1")
    #     frame2 = PhotoImage(file='listening.gif', format="gif -index 2")
    #     frame3 = PhotoImage(file='listening.gif', format="gif -index 3")
    #     frame4 = PhotoImage(file='listening.gif', format="gif -index 4")
    #     frame5 = PhotoImage(file='listening.gif', format="gif -index 5")
    #     frame6 = PhotoImage(file='listening.gif', format="gif -index 6")
    #     frame7 = PhotoImage(file='listening.gif', format="gif -index 7")
    #     frame8 = PhotoImage(file='listening.gif', format="gif -index 8")
    #     frame9 = PhotoImage(file='listening.gif', format="gif -index 9")
    #
    #     self.w = Label(parent, image=self.photo)
    #     self.w.configure(image=nextframe)
    #     self.w.photo = self.photo
    #     self.w.pack(side=TOP, anchor=W)
    #
    # frames = [PhotoImage(file='listening.gif', format='gif -index %i' % (i)) for i in range(100)]
    #
    # def update(ind):
    #     frame = frames[ind]
    #     ind += 1
    #     label.configure(image=frame)
    #     root.after(100, update, ind)
