# -*-coding: utf-8-*-
import requests
import traceback

from HTMLParser import HTMLParser


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


# HTMLParser wrapper
class HTMLParserWrapper(HTMLParser, object):
    pass


# HTML Library
class LibraryHTML(HTMLParserWrapper):
    def __init__(self):
        super(LibraryHTML, self).__init__()

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        pass

    def handle_endtag(self, tag):
        pass


# search book from library
@handle_exception
def search_book(keyword):
    url = "http://library.sejong.ac.kr/search/Search.IntResult.ax"

    params = {
        'q': keyword
    }

    source = requests.get(url, data=params).text

    print(source)

    lh = LibraryHTML()
    lh.feed(source)
    result = lh.result
    del lh

    return result

search_book(u'프로그래밍')
