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


class Quotes(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.quote = ''
        #self.quoteLbl = Text(self, font=('Verdana', smallText), fg="white", bg="black", height=4, width=50)
        self.quoteLbl = Label(self, font=('Verdana', smallText), fg="white", bg="black", height=5, width=50, wraplength=500)
        self.quoteLbl.pack(side=TOP, anchor=N)

        self.quotes_get()

    def quotes_get(self):
        try:
            url = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
            res = requests.get(url)
            # print res
            s = res.text
            s.replace('\r\n', '')
            s.replace("\'", "'")
            data = json.loads(s)
            #self.quoteLbl.insert(END, data["quoteText"] + "\n" + "- " + data["quoteAuthor"])

            quote = data["quoteText"] + "\n" + "- " + data["quoteAuthor"]
            self.quote = quote
            self.quoteLbl.config(text=quote)
            # print data
            # print self.data_get(self.data_fetch(url))
        except IOError:
            print('no internet')
        except ValueError:
            quote = "You miss 100% of the shots you don't take." + "\n" + "- Wayne Gretzky"
            self.quoteLbl.config(text=quote)