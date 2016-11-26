﻿# -*- coding: utf-8 -*-
import sys
import os

try:
    import telebot
except ImportError:
    sys.path.append(os.getcwd())
    import telebot

    from telebot.sejong import easteregg
    from telebot.sejong import volunteer
    from telebot.sejong import cvesearch
    from telebot.sejong import studyroom

#print easteregg.crawlInsta()
#print volunteer.getVolunteerInternal()


# volunteer
volE = volunteer.getVolunteerExternal()
volI = volunteer.getVolunteerInternal()

# External Univ
for vol in volE:
	print vol['title']

# Internal Univ
for vol in volI:
	print vol['title']
	print vol['date']
	print vol['time']

exit()

# cve search
cs = CVESearch()
result = cs.search_by_number('2016-1111')
print result

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
