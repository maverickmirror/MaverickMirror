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
import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as mp
import pandas as pd
import pandas_datareader.data as wb

globalStockMarketNews = True # stock market
xLargeText = 80
largeText = 56
mediumText = 28
smallText = 15

class headLines(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', smallText), fg="white", bg="black")
        self.eventNameLbl.pack(side=BOTTOM, anchor=N)

class stockMarket(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')     # background color
        self.title = 'Wells Fargo Stock' # 'google news' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', smallText), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.getStockMarket()

    # get the world news information method
    # parse it, check if a title exist, then result the specified number of google news titles.
    def getStockMarket(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()

            # number of days
            nOfDays = 2

            # todays date
            now = dt.datetime.now()

            # changing days, auto update days
            # today - 2 days
            start = now - timedelta(days=nOfDays)

            # wells fargo stock name
            stockName = 'WFC'

            # get wells fargo data from yahoo
            WellsFarsoStockMarket = wb.DataReader(stockName, 'yahoo', start, now)


            # display Yahoo
            headline = headLines(self.headlinesContainer, WellsFarsoStockMarket.head())
            headline.pack(side=TOP, anchor=W)

        except Exception as stock_number:
            traceback.print_exc()
            print ("Error: %s. Cannot get the stock ." % stock_number)

        # update news display every 30 minutes
        self.after(180, self.getStockMarket)
