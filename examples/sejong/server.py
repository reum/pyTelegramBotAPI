#-*- coding: utf-8 -*-
import sys, os

try:
    import telebot
except ImportError:
    sys.path.append(os.getcwd())
    import telebot
    from telebot.sejong import *

try:
    from api_token import API_TOKEN
except ImportError as e:
    API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

def sroom_error(e, message):
    print message

# Handle '/sroom' 
@bot.set_error_handler(sroom_error)
@bot.message_handler(commands=['sroom'])
def search_sroom(message):
    p = utils.Parser(" ".join(message.text.split(" ")[1:]))
    p.setAssum(int, "year", ["-y", "y"])
    p.setAssum(int, "month", ["-m", "m"])
    p.setAssum(int, "date", ["-d", "d"])
    p.setAssum(str, "time", ["-t", "t"])

    p.setType(int,0)
    p.setType(int,1)
    p.setType(int,2)

    rs = studyroom.RoomStatus.instance()
    """if len(p) == 0:
        pass
    elif len(p) == 2: # date, time
        pass
    elif len(p) == 3: # month, date, time
        pass
    elif len(p) == 4: # year, month, date, time
        pass
    else:
    """
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
        """try:
            rst = rs.search(p["year"], p["month"], p["date"], p["time"])
        except:
           """ 
        bot.reply_to(message, "Error!! %s" %(message.text,))


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.set_error_handler(sroom_error)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    s = dict()
    print s[1]
    bot.reply_to(message, message.text)


bot.polling()

"""

@bot.error_handler()
def Error():
    pass


@bot.error_handler(APIError, func=sroom)
def api_sroom_error(message, e):
    logging()
    bot.reply_to(message, e.error_message)



"""
