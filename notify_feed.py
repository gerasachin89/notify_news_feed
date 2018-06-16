import feedparser
import notify2
import os
import time

def feednotifier(news_feed_url, interval):
    """
       This method will parse the data from the URL and notify the User
    """
    # this will parse the news data from the URL. data will be in the form of dictionary
    #news_feed_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
    feeds = feedparser.parse(news_feed_url)
    # accessing the news feed from parse data"
    notify2.init('News Notify')
    for newsitem in feeds['items']:
        new_notification = notify2.Notification(newsitem['title'],
                                 newsitem['summary'],
                                 )
        new_notification.set_urgency(notify2.URGENCY_CRITICAL)
        new_notification.show()
        time.sleep(interval)

# calling feednotifier method with args and kwargs
# news_feed_url- subscribed news URL
# interval- time interval between 2 notifications
news_feed_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
feednotifier(news_feed_url,interval=100)
