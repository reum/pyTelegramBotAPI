# -*- coding: utf-8 -*-
import sys
import os

try:
    import telebot
except ImportError:
    sys.path.append(os.getcwd())
    sys.path.append("../../")
    import telebot

    from telebot.sejong import easteregg
    from telebot.sejong import volunteer
    from telebot.sejong.cvesearch import CVESearch
    from telebot.sejong import library
    from telebot.sejong import studyroom
    from telebot.sejong import news
    from telebot.sejong import rain

#rain
print rain.weather()

# Easter EGG
# iu_insta = easteregg.Insta("dlwlrma")
# print iu_insta.getImage()
# youtube = easteregg.getIUYoutube("IU_playlist.json")
# print youtube['title'], "|", youtube['url']

# Volunteer
print volunteer.getVolunteerInternal()
print volunteer.getVolunteerExternal()
exit(0)

# Volunteer
volE = volunteer.getVolunteerExternal()
volI = volunteer.getVolunteerInternal()

for vol in volE:
	print vol['title']

for vol in volI:
	print vol['title']
	print vol['date']
	print vol['time']




# library keyword search
print library.search_book(u'프로그래밍')

# cve search
cs = CVESearch()
result = cs.search_by_number('2016-1111')
print result

#SecuNews
newsList = news.getNews('news_issue')
newsText = ""
for news in newsList:
    newsText += "<"+news['index']+">"+'\n'
    newsText += "["+news['title']+"]"+'\n'
    newsText += news['description']+"..."+'\n'
    newsText += u"링크 : "+news['link']+'\n\n'
newsText = newsText[:4096]
print newsText 


# Study room search
rs = studyroom.RoomStatus.instance()
rs.cache_exp_sec = 120

# usage 1
rs.update(2016, 10)
print rs.search(2016,10,12,10)
print rs.search(2016,10,12,11)

# cache test
rs.update(2016, 10)
print rs.search(2016,10,12,12)
print rs.search(2016,10,12,13)

# usage 2
print rs.search(2016,10,12,range(10, 10+4))

# usage 3
print rs.mappingResult(rs.search(2016,10,12,range(10, 10+4)))

