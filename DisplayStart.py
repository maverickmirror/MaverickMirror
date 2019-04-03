from tkinter import *
from tkinter import ttk
from Services.TimeService import Clock
from Services.NewsFeedService import googleNews
from Services.WeatherService import Weather
from Services.QuoteService import Quotes
from Message import Message



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


class DisplayStart:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Start Screen")
        # self.v = self.tk.IntVar()
        self.tk.configure(background='black')
        self.tk.attributes("-fullscreen", True, '-topmost', True)
        #self.top.attributes('-topmost', True)
        # Create locations on the screen
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        #self.leftFrame = Frame(self.top, background='orange')
        #self.rightFrame = Frame(self.top, background='green')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        #self.leftFrame.pack(side=LEFT, fill=BOTH, expand=YES)
        #self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=YES)

        self.state = False
        # Binds Return key to toggle fullscreen on/off
        self.tk.bind("<Return>", self.toggle_fullscreen)
        # Binds Escape key to close fullscreen
        self.tk.bind("<Escape>", self.close_fullscreen)

        # initialize Clock
        # creates clock and sets location on screen
        self.clock = Clock(self.bottomFrame)
        self.clock.pack(side=BOTTOM, anchor=E, padx=50, pady=50)

        self.message = Message(self.topFrame)
        self.message.pack(side=BOTTOM, anchor=N, padx=0, )






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
    x = DisplayStart()
    x.tk.mainloop()
