# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:03:05 2019

@author: Zach's
"""
from tkinter import *
import time
import requests
import json
import traceback
import feedparser

twitterFeed = True
twitterFontSize = 10


class Twitter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')  # background color
        self.title = 'Twitter List'  
        self.twitterLbl = Label(self, text=self.title, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.twitterLbl.pack(side=TOP, anchor=W)
        self.twitterContainer = Frame(self, bg="black")
        self.twitterContainer.pack(side=TOP)
        self.getTwitter()

    # get the Twitter List
    def getTwitter(self):
        try:
            # remove all children
            for widget in self.twitterContainer.winfo_children():
                widget.destroy()
            # if the twitter is true, then run this problem
            if (twitterFeed):
                # parsed a user created twitter list
                twitterFeedparsed = feedparser.parse("https://wrk.pblc.it/twitter-rss-feed-generator/api/twitter2rss?url=YlpubDYyT01QS0xDUWRsRFh3UzJldlRxbGt3TERmblVCR285TzM1UldMSHY5VlpPc283QlpXS0pZdkdiQi9Qbw==")
                
                # if a title exist, then run top 5 twitter headlines for certain list;
                #if ('description' in twitterFeedparsed.feed):
                for post in twitterFeedparsed.entries[0:5]:
                        
                    twitterlist = twitterList(self.twitterContainer, post.title, post.description)
                    twitterlist.pack(side=TOP, anchor=E)

                                
        except Exception as twitterException:
            traceback.print_exc()
            print("Error: %s. Cannot get the twitter information." % twitterException)

        
        self.getTwitter
class twitterList(Frame):
    def __init__(self, parent, event_name="",event_name2=""):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', twitterFontSize), fg="white", bg="black")
        self.eventNameLbl.pack(side=BOTTOM, anchor=N)
        self.eventName2 = event_name2
        self.eventNameLbl2 = Label(self, text=self.eventName2, font=('Helvetica', twitterFontSize), fg="white", bg="black")
        self.eventNameLbl2.pack(side=BOTTOM, anchor=N)
        


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
        
        
        
        self.Twitter = Twitter(self.topFrame)
        self.Twitter.pack(side=BOTTOM, anchor=W, padx=100, pady=10)

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
        
        
        