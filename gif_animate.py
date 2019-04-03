from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import cImage

xLargeText = 80
largeText = 56
mediumText = 28
smallText = 11

class Animation(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.parent = parent
        self.canvas = Canvas(parent, width=80, height=80, bg='black', highlightthickness=0)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open('smallLoading.gif'))]
        self.image = self.canvas.create_image(40, 40, image=self.sequence[0])
        self.animate(1)
        self.label = Label(self, text='listening', font=("MS Sans Serif", smallText), fg="white", bg="black")
        self.label.pack(side=TOP, anchor=N, padx=70, )

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(38, lambda: self.animate((counter+1) % len(self.sequence)))

#
# root = Toplevel()
# app = Animation(root)
# root.mainloop()

