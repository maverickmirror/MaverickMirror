from Services import UserService
import tkinter
from tkinter.constants import *


class FrameService:
    # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/frame.html

    def __init__(self, userProfile):
        self.userProfile = userProfile
        self.frame = tkinter.Tk()

    # def quit(self):


if __name__ == '__main__':
    # myUserProfile = UserService()
    # UserService should have methods to implement NewsService, TimeService, and WeatherService
    # myUserProfile.???
    # myDisplay = FrameService(myUserProfile)
    # Example(Hello, World):

    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)
    label = tkinter.Label(frame, text="Hello, World")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame, text="Exit", command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()
