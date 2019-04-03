from tkinter import *
from tkinter import ttk
from Services.TimeService import Clock
from Services.NewsFeedService import googleNews
from Services.WeatherService import Weather
from Services.QuoteService import Quotes
from Services.StocksService import stockMarket





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


class Display2:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("Second Custom Profile")
        # self.v = self.tk.IntVar()
        self.top.configure(background='black')
        self.top.attributes("-fullscreen", True, '-topmost', True)
        #self.top.attributes('-topmost', True)
        # Create locations on the screen
        self.topFrame = Frame(self.top, background='black')
        self.bottomFrame = Frame(self.top, background='black')
        #self.leftFrame = Frame(self.top, background='orange')
        #self.rightFrame = Frame(self.top, background='green')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        #self.leftFrame.pack(side=LEFT, fill=BOTH, expand=YES)
        #self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=YES)

        self.state = False
        # Binds Return key to toggle fullscreen on/off
        self.top.bind("<Return>", self.toggle_fullscreen)
        # Binds Escape key to close fullscreen
        self.top.bind("<Escape>", self.close_fullscreen)

        # initialize Clock
        # creates clock and sets location on screen
        self.clock = Clock(self.bottomFrame)
        self.clock.pack(side=RIGHT, anchor=E, padx=70,)

        # initialize Weather
        # creates weather and sets location on screen
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=RIGHT, anchor=N, padx=100, pady=60)

        # initialize world News
        # creates news and show it on the screen
        #self.myNews = googleNews(self.topFrame)
        #self.myNews.pack(side=TOP, anchor=W, padx=100, pady=200)

        self.myStock = stockMarket(self.topFrame)
        self.myStock.pack(side=TOP, anchor=W, padx=100, pady=200)

        #initialize quote
        #create quote and show it on the screen
        self.quote = Quotes(self.bottomFrame)
        self.quote.pack(side=LEFT, anchor=W, padx=100,)

    def toggle_fullscreen(self, event=None):
        # toggles fullscreen and windowed
        # changes self.state to opposite value aka toggles it
        self.state = not self.state
        self.top.attributes("-fullscreen", self.state)
        return "break"

    def close_fullscreen(self, event=None):
        # exits out of fullscreen
        # sets self.state to False (off)
        self.state = False
        self.top.attributes("-fullscreen", False)
        return "break"


if __name__ == '__main__':
    x = Display2()
    x.top.mainloop()
