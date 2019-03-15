# Magic Mirror Main File
# created 03/14/19

from tkinter import *
import time


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
