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


weatherAPIToken = '6d60a7966b8e994764a623080558cf19'
weatherLang = 'en'
weatherUnit = 'us'
latitude = '44.1634663'
longitude = '-93.9993505'

xLargeText = 80
largeText = 56
mediumText = 28
smallText = 18


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
            # if the googleNews is true, then run this problem
            if (globalNews):
                # parsed a google news rss website
                googleNewsFeedparsed = feedparser.parse("https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en")

                # if a title exist, then run top 3 news headlines;
                if ('title' in googleNewsFeedparsed.feed):
                    for post in googleNewsFeedparsed.entries[0:3]:
                        headline = headLines(self.headlinesContainer, post.title)
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
