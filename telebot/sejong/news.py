#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib

def getNews(command):

    if command == 'news_issue':
        try:
            r = urllib.urlopen('http://www.dailysecu.com/rss/S1N1.xml').read()
        except urllib.error.HTTPError as e:
            error_message = "Error %s HTTP." % e.code
            return error_message
    elif command == 'news_popular':
        try:
            r = urllib.urlopen('http://www.dailysecu.com/rss/clickTop.xml').read()
        except Exception as e:
            error_message = "Error %s HTTP." % e.code
            return error_message

    soup = BeautifulSoup(r, "html.parser")
    newsItems = soup.find_all("item")

    newsList = []
    newsDict = {}

    i=1
    for newsItem in newsItems:
        if i==11:
            return newsList
        else:
            title = newsItem.find("title").get_text()
            description = newsItem.find("description").get_text()
            link = newsItem.find("link").get_text()
            
            newsDict['index']  = str(i)
            newsDict['title']  = title                # title
            newsDict['description'] = description     # news description
            newsDict['link'] = link                   # link to news
            
            newsList.append(newsDict)
            newsDict = {}
            i=i+1   

    return newsList

