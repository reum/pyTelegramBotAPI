#-*- coding: utf-8 -*-
import sys, os

try:
    import telebot
except ImportError:
    sys.path.append(os.getcwd())
    import telebot

    from telebot.sejong import utils
    from telebot.sejong import easteregg
    from telebot.sejong import volunteer
    from telebot.sejong import studyroom

    
# Parser Test

a = utils.Parser("-y 2016 -m 11 -d 22")

a.setAssum(int, "date", ["-d", "d", "date"])
print a["date"]

a.setAssum(int, "month", ["-m", "m", ])
print a["month"]

a = utils.Parser("-t dlwlrma")
a.setAssum(str, "target", ["-t", "t"])
print a["target"]



b = utils.Parser("2016 11 22")
print type(b[0]), b[0]
b.setType(int, 0)
print type(b[0]), b[0]


print easteregg.crawlInsta()
print volunteer.getVolunteerInternal()

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

