# -*- coding: utf-8 -*-
import sys
import os
import re
import random

try:
    import telebot1
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
    from telebot.sejong import rain

    from telebot import types

    from telebot.sejong import utils

try:
    from api_token import API_TOKEN
except ImportError as e:
	API_TOKEN = '<api_token>'
   
#################
bot = telebot.TeleBot(API_TOKEN)
#################

# help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    help_info = """
@OSSBeemoBot 사용법
======================================
/help : 도움말 출력
/credit : 제작자 출력 (알파벳순)
/news : 정보보안 뉴스 보기
/vol : 세종사회봉사 리스트 보기
/iu : 아이유 사진 / 음악 출력
/cve <CVE-를 제외한 CVE ID> : CVE 번호에 해당하는 정보 출력
/library <키워드> : 키워드에 해당하는 책 리스트 및 대출 가능여부 출력
/weather: 강수확률 + 메시지 출력
/sroom <year> <month> <day> <time_range> : 해당 시간에 대여가능한 스터디룸 목록 출력
======================================
    """
    bot.reply_to(message, help_info)


# Weather
@bot.message_handler(commands=['weather'])
def send_weather(message):
    result = rain.weather()
    bot.reply_to(message, result)

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


# credit
@bot.message_handler(commands=['credit'])
def credit_info(message):
    credit_text = """
@bunseokbot, @daeunim, @jsh95311, @reum, @sweetchipsw
Class : Open Source Software
Github : https://github.com/reum/pyTelegramBotAPI/
    """

    bot.reply_to(message, credit_text)

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)
#    print message
@bot.message_handler(commands=['sroom'])
def search_sroom(message):
    args = message.text.split(" ")[1:]
    rs = studyroom.RoomStatus.instance()
    print "asd"
    if len(args) == 3:
        args.insert(0, "2016") # TODO

    if '~' in args[3] :
        s, e = args[3].split('~')
    elif '-' in args[3] :
        s, e = args[3].split('-')
    else:
        s = e = args[3]

    try:
        s = int(s)
        e = int(e)
        rst = rs.mappingResult(rs.search(int(args[0]),int(args[1]),int(args[2]),range(s,e+1)))
        bot.reply_to(message, ", ".join(rst))
    except:
        bot.reply_to(message, "Error!! %s" %(message.text,))

if __name__ == '__main__':
	
    iu_insta = easteregg.Insta("dlwlrma")
    iu_youtube = easteregg.IUYoutube()
    iu_youtube.setJsonFile("IU_playlist.json")

    bot.polling(none_stop=False, interval=1)

