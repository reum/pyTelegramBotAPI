# -*- coding: utf-8 -*-
import sys
import os
import random

try:
    import telebot
except ImportError:
    sys.path.append("../../")
    sys.path.append(os.getcwd())
    import telebot

    from telebot.sejong import easteregg
    from telebot.sejong import volunteer
    from telebot.sejong import cvesearch
    from telebot.sejong import studyroom
    from telebot.sejong import news
    from telebot import types

try:
    from api_token import API_TOKEN
except ImportError as e:
	API_TOKEN = '276556030:AAGwUMBx9fkUMmISaJSZY7Zy3Rc6krjM7Z8'

   
#################
bot = telebot.TeleBot(API_TOKEN)
#################

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Easteregg
@bot.message_handler(commands=['iu'])
def send_easteregg(message):
    i = random.randint(0, 1)
    if i == 0:
        fname_photo = iu_insta.getImage()
        photo = open('./insta_images/'+fname_photo, 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        youtube = iu_youtube.getIUYoutube()
        youtube_str = u"오늘의 음악추천 : "+youtube['title']+ u"\nURL :"+ youtube['url']
        bot.reply_to(message, youtube_str)

# Sejong Volunteer
@bot.message_handler(commands=['vol'])
def send_volunteerinfo(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton(u'/외부봉사')
    itembtnv = types.KeyboardButton(u'/내부봉사')
    markup.row(itembtna, itembtnv)
    bot.send_message(chat_id, "Choose volunteer:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == u'/내부봉사' and message.content_type == 'text')
def send_volunteerinfo(message):
    chat_id = message.chat.id
    result = ""
    volInternal = volunteer.getVolunteerInternal()
    for vol in volInternal:
        result += "="*20+"\n"
        result += u"봉사 이름 :"+vol['title'] +"\n"
        result += u"봉사 기간 :"+vol['date']+u"("+vol['day']+u")"+"\n"
        result += u"봉사 시간 :"+vol['time']+"\n"
    bot.reply_to(message, result)

@bot.message_handler(func=lambda message: message.text == u'/외부봉사' and message.content_type == 'text')
def send_volunteerinfo(message):
    chat_id = message.chat.id
    result = ""
    volInternal = volunteer.getVolunteerExternal()
    for vol in volInternal:
        result += u"봉사 이름 :"+vol['title']+"\n"
    bot.reply_to(message, result)



# News
@bot.message_handler(commands=['news'])
def send_news(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    btn_issue = types.KeyboardButton(u'/이슈기사')
    btn_popular = types.KeyboardButton(u'/인기기사')
    markup.row(btn_issue, btn_popular)
    bot.send_message(chat_id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == u'/이슈기사' and message.content_type == 'text')
def send_news(message):
    chat_id = message.chat.id
    newsList = news.getNews('news_issue')
    newsText = ""
    for newsItem in newsList:
        newsText += "<"+newsItem['index']+">"+'\n'
        newsText += "["+newsItem['title']+"]"+'\n'
        newsText += newsItem['description']+"..."+'\n'
        newsText += u"링크 : "+newsItem['link']+'\n\n'
    bot.reply_to(message, newsText)

@bot.message_handler(func=lambda message: message.text == u'/인기기사' and message.content_type == 'text')
def send_news(message):
    chat_id = message.chat.id
    newsList = news.getNews('news_popular')
    newsText = ""
    for newsItem in newsList:
        newsText += "<"+newsItem['index']+">"+'\n'
        newsText += "["+newsItem['title']+"]"+'\n'
        newsText += newsItem['description']+"..."+'\n'
        newsText += u"링크 : "+newsItem['link']+'\n\n'
    bot.reply_to(message, newsText)
	

# Default
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    print message

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)
#    print message


if __name__ == '__main__':
	
    iu_insta = easteregg.Insta("dlwlrma")
    iu_youtube = easteregg.IUYoutube()
    iu_youtube.setJsonFile("IU_playlist.json")

    bot.polling(none_stop=False, interval=1)

