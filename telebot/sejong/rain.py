#-*- coding:utf-8 -*-
import re
import xml.etree.ElementTree as ET
import urllib2

def weather():
   try:
      url = "http://www.kma.go.kr//wid/queryDFSRSS.jsp?zone=1121573000"
      data = ET.ElementTree(file=urllib2.urlopen(url))
      root = data.getroot()

   except Exception as e :
      error = "Error!!"
      return error   

   rain_prob = []
   x = 0
   n = []
   
   for data in root.iter("data"):
      if data.findtext("day")<'1' and data.findtext("pop")>='0' and data.findtext("pop")<='10':
         n.append(int(data.findtext("pop")))
         x = 1
      elif data.findtext("day")<'1' and data.findtext("pop")>='11' and data.findtext("pop")<='50':
         n.append(int(data.findtext("pop")))
         x = 2
      elif data.findtext("day")<'1' and data.findtext("pop")>='51' and data.findtext("pop")<='100':
         n.append(int(data.findtext("pop")))
         x = 3
      elif data.findtext("day")!='0' and data.findtext("day")<'2' and data.findtext("pop")>='0' and data.findtext("pop")<='10':
         n.append(int(data.findtext("pop")))
         x = 4
      elif data.findtext("day")!='0' and data.findtext("day")<'2' and data.findtext("pop")>='11' and data.findtext("pop")<='50':
         n.append(int(data.findtext("pop")))
         x = 5
      elif data.findtext("day")!='0' and data.findtext("day")<'2' and data.findtext("pop")>='51' and data.findtext("pop")<='100':
         n.append(int(data.findtext("pop")))
         x = 6   
   if x == 1 or x == 4 :
      rain_prob = "강수확률 : %s%%\n비 안 온대"%max(n)
   elif x == 2 or x == 5 :
      rain_prob = "강수확률 : %s%%\n비올 것 같아"%max(n)
   elif x == 3 or x == 6 :
      rain_prob = "강수확률 : %s%%\n우산 챙기렴"%max(n)
   
   return rain_prob
