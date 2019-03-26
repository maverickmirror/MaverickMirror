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

class Weather(Frame):
    def __init__(self, parent, *args, **kargs):
        Frame.__init__(self, parent, bg='black')

        #intialize needed vairbles
        self.currently = ''
        self.icon = ''

        #create frame for the weather
        self.degreeFrm = Frame(self, bg='black')
        self.degreeFrm.pack(side=TOP, anchor=E)

        #create temperature and change attributes (font, size, color)
        self.temperature = ''
        self.temperatureLb1 = Label(self.degreeFrm, font=('Verdana', xLargeText), fg="white", bg="black")
        self.temperatureLb1.pack(side=TOP, anchor=E)

        # create current condition label and change attributes (font, size, color)
        self.currentlyLbl = Label(self, font=('Verdana', mediumText), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=E)

        # create forecast and change attributes (font, size, color)
        self.forecast = ''
        self.forecastLbl = Label(self, font=('Verdana', smallText), fg="white", bg="black")
        self.forecastLbl.pack(side=TOP, anchor=E)

        # create location and change attributes (font, size, color)
        self.location = ''
        self.locationLbl = Label(self, font=('Verdana', smallText), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=E)

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