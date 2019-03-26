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
smallText = 18


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        # create clock face and change attributes (font, size, color)
        self.time = ''
        self.timeLabel = Label(self, font=("Verdana", largeText), fg="white", bg="black")
        # sets location on screen and orientation
        self.timeLabel.pack(side=TOP, anchor=N)

        # create day of week and change attributes (font, size, color)
        self.dayOfWeek = ''
        self.dayLabel = Label(self, font=("Verdana", smallText), fg="white", bg="black")
        # sets location on screen and orientation
        self.dayLabel.pack(side=TOP, anchor=E)

        # create date and change attributes (font, size, color)
        self.date = ''
        self.dateLabel = Label(self, font=("MS Sans Serif", smallText), fg="white", bg="black")
        # sets location on screen and orientation
        self.dateLabel.pack(side=TOP, anchor=E)

        self.tick()

    def tick(self):
        # set formatting for time, day, and date
        timeFormat = time.strftime('%I:%M %p').lstrip('0')

        dayOfWeekFomat = time.strftime('%A')

        dateFormat = time.strftime("%b %d, %Y")

        # sets time, day, date to correct format

        if timeFormat != self.time:
            self.time = timeFormat
            self.timeLabel.config(text=timeFormat)

        if dayOfWeekFomat != self.dayOfWeek:
            self.dayOfWeek = dayOfWeekFomat
            self.dayLabel.config(text=dayOfWeekFomat)

        if dateFormat != self.date:
            self.date = dateFormat
            self.dateLabel.config(text=dateFormat)

        self.timeLabel.after(200, self.tick)
