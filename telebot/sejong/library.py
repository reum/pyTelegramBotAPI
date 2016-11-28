# -*-coding: utf-8-*-
import requests
import re
import traceback

from bs4 import BeautifulSoup


# exception handler decorator
def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except:
            print(traceback.format_exc())
            result = None
        finally:
            return result
    return wrapper


# search book from library
@handle_exception
def search_book(keyword):
    url = "http://library.sejong.ac.kr/search/Search.Result.ax?"\
          "?sid=1&q=%s" % keyword

    source = requests.get(url).text

    result = []

    soup = BeautifulSoup(source, 'html.parser')

    for a in soup.find_all('a'):
        href = a.get("href")
        if re.match('javascript:search.goDetail\([0-9]{6,8}\);', href):
            result.append({'bookName': a.get_text().strip()})

    # counter variable in for loop
    cnt = 0

    for p in soup.find_all('p', attrs={"class": "tag"}):
        # bookid, bookstatus
        bid, stat = p.get_text().split('\n')[2].replace('\t', '').strip().split('   ')
        result[cnt]['bookId'] = bid
        result[cnt]['bookStatus'] = stat
        cnt += 1

    return result
