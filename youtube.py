class Youtube(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')  # background color
        self.title = 'Powerful JRE recent uploads'  
        self.youtubeLbl = Label(self, text=self.title, font=('Helvetica', newsFontSize), fg="white", bg="black")
        self.youtubeLbl.pack(side=TOP, anchor=W)
        self.youtubeContainer = Frame(self, bg="black")
        self.youtubeContainer.pack(side=TOP)
        self.getYoutube()

    # get the Youtube subscriptions titles
    # parse it, check if a title exist, then result the specified number of PowerfulJRE titles.
    def getYoutube(self):
        try:
            # remove all children
            for widget in self.youtubeContainer.winfo_children():
                widget.destroy()
            # if the youtube is true, then run this problem
            if (youtubeVideos):
                # parsed a Youtube popular rss website
                youtubeVideosFeedparsed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCzQUP1qoWDoEbmsQxvdjxgQ")
                
                # if a title exist, then run top 3 news headlines;
                if ('title' in youtubeVideosFeedparsed.feed):
                    for post in youtubeVideosFeedparsed.entries[0:5]:
                        
                        trending = Trending(self.youtubeContainer, post.title, post.media_thumbnail)
                        trending.pack(side=TOP, anchor=W)

                                
        except Exception as youtubeVideosException:
            traceback.print_exc()
            print("Error: %s. Cannot get the youtube videos." % youtubeVideosException)

        # update PowerfulJRE every 30 minutes
        self.getYoutube
class Trending(Frame):
    def __init__(self, parent, event_name="",event_name2=""):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', youtubeFontSize), fg="white", bg="black")
        self.eventNameLbl.pack(side=BOTTOM, anchor=N)
        self.eventName2 = event_name2
        self.eventNameLbl2 = Label(self, text=self.eventName2, font=('Helvetica', youtubeFontSize), fg="white", bg="black")
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
        
        
        
        self.Youtube = Youtube(self.topFrame)
        self.Youtube.pack(side=BOTTOM, anchor=W, padx=100, pady=10)

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
        
        
        