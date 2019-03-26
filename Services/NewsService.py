# import feedparser and schedule
import feedparser
import schedule


# all news headline titles
class NewsService():

    def __init__ (self):

        #  get new
        def getNews():
            # parse google news website
            webfeedParsed = feedparser.parse("https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en")

            # check if the title exist
            if ('title' in webfeedParsed.feed):
                # get the top 5 in google news
                for i in webfeedParsed.entries[0:5]:
                    #  print the news title
                    print(i.title + "\n")

        getNews()

        # scheduled to return the google news feed parser evety 3 minutes to get the
        #  the news updates.
        def updateNews():
            x = True
            # run every 3 minutes
            schedule.every(3).minutes.do(getNews())

            while x:
                schedule.run_pending()

NewsService()


