#-*- coding: utf-8 -*-
import sys, os

try:
    import telebot
except ImportError:
    sys.path.append(os.getcwd())
    import telebot

    from telebot.sejong import easteregg
    from telebot.sejong import volunteer
    from telebot.sejong import library

print easteregg.crawlInsta()
print volunteer.getVolunteerInternal()

print library.search_book(u'프로그래밍')
