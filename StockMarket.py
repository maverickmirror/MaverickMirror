'''
import datetime as dt
from datetime import timedelta
import  matplotlib.pyplot as mp
import pandas as pd
import  pandas_datareader.data as wb


def getStockMarket():

    nOfDays = 2

    now = dt.datetime.now()
    start = now -timedelta(days=nOfDays)

    stockName ='AAPL'

    appleStockMarket = wb.DataReader(stockName, 'yahoo', start, now)

    print(appleStockMarket.head())

getStockMarket()

'''

# Magic Mirror Main File
# created 03/14/19

from tkinter import *
import time
import requests
import json
import traceback
import feedparser
import schedule



globalNews = True  # google news
globalStockMarketNews = True # stock market
newsFontSize = 15 # font size for the google news and stock market news

import datetime as dt
from datetime import timedelta
import  matplotlib.pyplot as mp
import pandas as pd
import  pandas_datareader.data as wb

''' 
# google news class
class googleNews(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')     # background color
        self.title = 'World news' # 'google news' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.getNews()

    # get the world news information method
    # parse it, check if a title exist, then result the specified number of google news titles.
    def getNews(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()

            nOfDays = 1

            now = dt.datetime.now()
            start = now - timedelta(days=nOfDays)

            stockName = 'AAPL'

            appleStockMarket = wb.DataReader(stockName, 'yahoo', start, now)



            headline = headLines(self.headlinesContainer, appleStockMarket.tail())
            headline.pack(side=TOP, anchor=W)

        except Exception as googleNewsException:
            traceback.print_exc()
            print ("Error: %s. Cannot get the google news." % googleNewsException)

        # update news display every 30 minutes
        self.after(1800, self.getNews)




class headLines(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.eventNameLbl.pack(side=BOTTOM, anchor=N)
'''




class stockMarket(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')     # background color
        self.title = 'My stock Market' # 'google news' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', newsFontSize), fg="white", bg="black")
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

            nOfDays = 2

            now = dt.datetime.now()
            start = now - timedelta(days=nOfDays)

            stockName = 'WFC'

            appleStockMarket = wb.DataReader(stockName, 'yahoo', start, now)

            # print(appleStockMarket.head())

            headline = headLines(self.headlinesContainer, appleStockMarket.head())
            headline.pack(side=TOP, anchor=W)

        except Exception as googleNewsException:
            traceback.print_exc()
            print ("Error: %s. Cannot get the google news." % googleNewsException)

        # update news display every 30 minutes
        self.after(1800, self.getStockMarket)




class headLines(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.eventNameLbl.pack(side=BOTTOM, anchor=N)


class Display:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.tk.attributes("-fullscreen", True)
        # Create locations on the screen
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        # Binds Return key to toggle fullscreen on/off
        self.tk.bind("<Return>", self.toggle_fullscreen)
        # Binds Escape key to close fullscreen
        self.tk.bind("<Escape>", self.close_fullscreen)



        # initialize world News
        # creates news and show it on the screen
        self.myNews = stockMarket(self.bottomFrame)
        self.myNews.pack(side=BOTTOM, anchor=W, padx=100, pady=70)

        # self.myStock = googleNews(self.bottomFrame)
        # selfelf.myStock.pack(side=BOTTOM, anchor=W, padx=100, pady=70)


    def toggle_fullscreen(self, event=None):
        # toggles fullscreen and windowed
        # changes self.state to opposite value aka toggles it
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def close_fullscreen(self, event=None):
        # exits out of fullscreen
        # sets self.state to False (off)
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


if __name__ == '__main__':
    x = Display()
    x.tk.mainloop()

#
# import pandas as p
# import quandl
# import datetime as dt
#
#
# nOfDays = 2
#
# now = dt.datetime.now()
# start = now - dt.timedelta(days=nOfDays)
#
# stock = "AAPL"
#
# apple = quandl.get("WIKI/" + stock, start_date=start, end_date=now)
# type(apple)
#
# p.core.frame.DateFrame
# apple.head()