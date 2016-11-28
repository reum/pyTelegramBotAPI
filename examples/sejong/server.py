# -*- coding: utf-8 -*-
import sys
import os
import re
import random

try:
    import telebot
except ImportError:
    sys.path.append("../../")
    sys.path.append(os.getcwd())
    import telebot

    from telebot.sejong import easteregg
    from telebot.sejong import volunteer
    from telebot.sejong.cvesearch import CVESearch
    from telebot.sejong import library
    from telebot.sejong import studyroom
    from telebot.sejong import news
    from telebot import types

try:
    from api_token import API_TOKEN
except ImportError as e:
<<<<<<< HEAD
	API_TOKEN = '276556030:AAGwUMBx9fkUMmISaJSZY7Zy3Rc6krjM7Z8'

=======
	API_TOKEN = '<api_token>'
>>>>>>> 6a4b0ff644226ac0ee5d9ed4e80f7e69032aaa94
   
#################
bot = telebot.TeleBot(API_TOKEN)
#################

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

<<<<<<< HEAD
# Easteregg
=======

@bot.message_handler(commands=['cve'])
def send_cvesearch(message):
    try:
        number = message.text.split(' ')[1]
    except:
        number = None

    c = CVESearch()
    result = c.search_by_number(number)
    del c

    if result is None:
        cve_str = u"비정상적인 CVE 번호이거나 존재하지 않는 번호입니다."
    else:
        cve_str = u"CVE-%s 검색 결과\n" % number
        cve_str += u"CVSS : %s\n" % result['cvss']
        cve_str += u"대상 벤더사 : %s\n" % ', '.join(result['vendor'])
        cve_str += u"취약점 분류 : %s\n" % result['vt_info']
        cve_str += u"취약점 설명 : %s\n" % result['summary']
        cve_str += u"최초 발견자 : %s\n" % result['credit']
        cve_str += u"상세 설명 : https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-%s" % number

    bot.reply_to(message, cve_str)


@bot.message_handler(commands=['library'])
def send_library(message):
    try:
        keyword = message.text.split(' ')[1]
    except:
        keyword = None

    result = library.search_book(keyword)

    if result is None:
        lib_str = u"비정상적인 키워드거나 검색 결과가 없습니다."

    else:
        lib_str = u"%s 키워드로 검색한 도서입니다\n" % keyword

        lib_str += u"===============================\n"

        for row in result:
            lib_str += u"도서명 : %s\n" % row['bookName']
            lib_str += u"도서 관리번호 : %s\n" % row['bookId']
            lib_str += u"대출 여부 : %s\n" % row['bookStatus']
            lib_str += u"===============================\n"

    bot.reply_to(message, lib_str)


>>>>>>> 6a4b0ff644226ac0ee5d9ed4e80f7e69032aaa94
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

<<<<<<< HEAD


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
=======
@bot.message_handler(commands=['sroom'])
def search_sroom(message):
    p = utils.Parser(" ".join(message.text.split(" ")[1:]))

    p.setType(int,0)
    p.setType(int,1)
    p.setType(int,2)

    rs = studyroom.RoomStatus.instance()
  
    if '~' in p[3] :
        s, e = p[3].split('~')
    elif '-' in p[3] :
        s, e = p[3].split('-')
    else:
        s = e = p[3]

    try:
        s = int(s)
        e = int(e)
        rst = rs.mappingResult(rs.search(p[0],p[1],p[2],range(s,e+1)))
        bot.reply_to(message, ", ".join(rst))
        print rst
    except:
        bot.reply_to(message, "Error!! %s" %(message.text,))

>>>>>>> 6a4b0ff644226ac0ee5d9ed4e80f7e69032aaa94


if __name__ == '__main__':
	
    iu_insta = easteregg.Insta("dlwlrma")
    iu_youtube = easteregg.IUYoutube()
    iu_youtube.setJsonFile("IU_playlist.json")

    bot.polling(none_stop=False, interval=1)

