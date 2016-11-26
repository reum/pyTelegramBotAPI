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
    url = "http://library.sejong.ac.kr/search/Search.IntResult.ax"\
          "?sid=&q={0}&qf={0}&qt={0}&wid=&tabID=&q1={0}&x=0&y=0&q2"\
          "=&q3=".format(keyword)

    source = requests.get(url).text

    print(source)

    lh = LibraryHTML()
    lh.feed(source)
    result = lh.result
    del lh

    return result
