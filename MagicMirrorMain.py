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



class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        # create clock face and change attributes (font, size, color)
        self.time = ''
        self.timeLabel = Label(self, font=("MS Sans Serif", largeText), fg="white", bg="black")
        # sets location on screen and orientation
        self.timeLabel.pack(side=TOP, anchor=N)

        # create day of week and change attributes (font, size, color)
        self.dayOfWeek = ''
        self.dayLabel = Label(self, font=("MS Sans Serif", smallText), fg="white", bg="black")
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

class Weather(Frame):
    def __init__(self, parent, *args, **kargs):
        Frame.__init__(self, parent, bg='black')

        #intialize needed vairbles
        self.currently = ''
        self.icon = ''

        #create frame for the weather
        self.degreeFrm = Frame(self, bg='black')
        self.degreeFrm.pack(side=TOP, anchor=W)

        #create temperature and change attributes (font, size, color)
        self.temperature = ''
        self.temperatureLb1 = Label(self.degreeFrm, font=('Verdana', xLargeText), fg="white", bg="black")
        self.temperatureLb1.pack(side=LEFT, anchor=N)

        # create current condition label and change attributes (font, size, color)
        self.currentlyLbl = Label(self, font=('Verdana', mediumText), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=W)

        # create forecast and change attributes (font, size, color)
        self.forecast = ''
        self.forecastLbl = Label(self, font=('Verdana', smallText), fg="white", bg="black")
        self.forecastLbl.pack(side=TOP, anchor=W)

        # create location and change attributes (font, size, color)
        self.location = ''
        self.locationLbl = Label(self, font=('Verdana', smallText), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=W)

        self.get_weather()



    def get_weather(self):
        try:


            location2 = ""

            # sets the weather to the correct location
            weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (weatherAPIToken, latitude, longitude, weatherLang, weatherUnit)

            # uses the url to get the weather
            r = requests.get(weather_req_url)
            weatherObject = json.loads(r.text)

            # takes all needed information from the weatherObject
            degreeSign = u'\N{DEGREE SIGN}'
            temperature2 = "%s%s" % (str(int(weatherObject['currently']['temperature'])), degreeSign)
            currently2 = weatherObject['currently']['summary']
            forecast2 = weatherObject["hourly"]["summary"]


            # sets the current conditions to the correct varibles
            if self.currently != currently2:
                self.currently = currently2
                self.currentlyLbl.config(text=currently2)
            if self.forecast != forecast2:
                self.forecast = forecast2
                self.forecastLbl.config(text=forecast2)
            if self.temperature != temperature2:
                self.temperature = temperature2
                self.temperatureLb1.config(text=temperature2)
            if self.location != location2:
                if location2 == ", ":
                    self.location = "Cannot Pinpoint Location"
                    self.locationLbl.config(text="Cannot Pinpoint Location")
                else:
                    self.location = location2
                    self.locationLbl.config(text=location2)

        # exception incase weather cannont be found
        except Exception as e:
            traceback.print_exc()
            print("Error: %s. Cannot get weather." % e)

        self.after(600000, self.get_weather)

        #converts from kelvin to fahrenheit if needed
        def convert_kelvin_to_fahrenheit(kelvin_temp):
            return 1.8 * (kelvin_temp - 273) + 32





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


class Quotes(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.quoteLbl = Text(self, font=('Helvetica', smallText), fg="white", bg="black", height=4, width=50)
        self.quoteLbl.pack(side=TOP, anchor=W)

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
            self.quoteLbl.insert(END, data["quoteText"] + "\n" + "- " + data["quoteAuthor"])

            # print data
            # print self.data_get(self.data_fetch(url))
        except IOError:
            print('no internet')


class Display:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
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

        # initialize Clock
        # creates clock and sets location on screen
        self.clock = Clock(self.bottomFrame)
        self.clock.pack(side=BOTTOM, anchor=E, padx=100, pady=60)

        # initialize Weather
        # creates weather and sets location on screen
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)

        # initialize world News
        # creates news and show it on the screen
        self.myNews = googleNews(self.bottomFrame)
        self.myNews.pack(side=BOTTOM, anchor=W, padx=100, pady=10)

        #initialize quote
        #create quote and show it on the screen
        self.quote = Quotes(self.topFrame)
        self.quote.pack(side=TOP, anchor=E, padx=100, pady=60)




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
