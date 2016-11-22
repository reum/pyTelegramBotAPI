import re
import xml.etree.ElementTree as ET
import requests
import urllib.request

from urllib.request import urlopen

url = "http://www.kma.go.kr//wid/queryDFSRSS.jsp?zone=1121573000"

data = requests.get(url)
	
tree = ET.parse(urlopen('http://www.kma.go.kr//wid/queryDFSRSS.jsp?zone=1121573000'))
root = tree.getroot()

def weather():
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
	if x == 1 :
		print("°­¼öÈ®·ü :",max(n),"%")
		print("ºñ¾È¿Â´ë")
	elif x == 2 :
		print("°­¼öÈ®·ü :",max(n),"%")
		print("ºñ¿ÃÁöµµ")
	elif x == 3 :
		print("°­¼öÈ®·ü :",max(n),"%")
		print("¿ì»êÃ¬±â·Å")
