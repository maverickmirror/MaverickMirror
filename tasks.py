from tkinter import *
import time
import requests
import json
import traceback
import feedparser
#import gdata
#import schedule

globalNews = True  # google news
globalStockMarketNews = True  # stock market
newsFontSize = 15  # font size for the google news and stock market news

youtubeVideos = True
youtubeFontSize = 10

weatherAPIToken = '6d60a7966b8e994764a623080558cf19'
weatherLang = 'en'
weatherUnit = 'us'
latitude = '44.1634663'
longitude = '-93.9993505'

xLargeText = 80
largeText = 56
mediumText = 28
smallText = 18







class Tasks(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')  # background color
        self.title = 'Tasks Today'  
        self.taskLbl = Label(self, text=self.title, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.taskLbl.pack(side=TOP, anchor=W)
        self.taskContainer = Frame(self, bg="black")
        self.taskContainer.pack(side=TOP)
        self.getTask()

    def getTask(self):
        self.dayOfWeek = ''
        dayOfWeekFomat = time.strftime('%A')
        
        if dayOfWeekFomat != self.dayOfWeek:
            self.dayOfWeek = dayOfWeekFomat
            
        
        try:
            
            for widget in self.taskContainer.winfo_children():
                    widget.destroy()
            if dayOfWeekFomat == 'Monday':
                    
                    myTasks = ['8am: IT380','10am: IT414','12pm: Work','5pm: Dinner','10pm: Lift'] 
                    for task in myTasks:
                        
                        todaystask= todaysTask(self.taskContainer, task)
                        todaystask.pack(side=TOP, anchor=W)
                    
                    
            if dayOfWeekFomat == 'Tuesday':
                    
                    myTasks = ['10am: IT450','12pm: Lunch','3pm: IT418','5pm: Dinner','10pm: Lift']
                    for task in myTasks:
                        
                        todaystask= todaysTask(self.taskContainer, task)
                        todaystask.pack(side=TOP, anchor=W)
                    
                    
            if dayOfWeekFomat == 'Wednesday':
                    
                   myTasks = ['8am: IT380','10am: IT414','12pm: Work','5pm: Dinner','10pm: Lift']
                   for task in myTasks:
                        
                        todaystask= todaysTask(self.taskContainer, task)
                        todaystask.pack(side=TOP, anchor=W)
                    
                    
            if dayOfWeekFomat == 'Thursday':
                    
                    myTasks = ['10am: IT450','12pm: Lunch','3pm: IT418','5pm: Dinner','10pm: Lift']
                    for task in myTasks:
                        
                        todaystask= todaysTask(self.taskContainer, task)
                        todaystask.pack(side=TOP, anchor=W)
                    
                    
            if dayOfWeekFomat == 'Friday':
                    
                    myTasks = ['9am: Work','12pm: Lunch','5pm: Dinner','10pm: Lift']
                    for task in mytasks:
                        
                        todaystask= todaysTask(self.taskContainer, myTasks)
                        todaystask.pack(side=TOP, anchor=W)
                    
                    
            if dayOfWeekFomat == 'Saturday':
                    
                    myTasks = ['Whatever you are feeling'] 
                    for task in myTasks:
                        
                        todaystask= todaysTask(self.taskContainer, task)
                        todaystask.pack(side=TOP, anchor=W)
                    
                    
            if dayOfWeekFomat == 'Sunday':
                    
                    myTasks = ['Homework'] 
                    for task in myTasks:
                        
                        todaystask= todaysTask(self.taskContainer, task)
                        todaystask.pack(side=TOP, anchor=W)
                    
        except Exception as task_fail:
                traceback.print_exc()
                print ("Error: %s. Cannot get tasks ." % task_fail)

        
        
class todaysTask(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.eventNameLbl.pack(side=BOTTOM, anchor=N)
        
        
        
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
        

        
        self.Tasks = Tasks(self.topFrame)
        self.Tasks.pack(side=BOTTOM, anchor=W, padx=100, pady=10)
        
        
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