# -*-coding:UTF-8-*-

from html.parser import HTMLParser
from urllib.request import Request,urlopen
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._current_data = ''
        self._cont = False

    def handle_starttag(self, tag, attrs):
        self._current_data = tag
        if tag in ['br', 'p']:
            self._cont = True
        else:
            self._cont = False
    #
    def handle_endtag(self, tag):
        self._current_data = ''
    #

    def handle_data(self, data):
        if self._current_data in ['p', 'title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br'] and len(data) > 1:
            if self._cont:
                print(data, end='')
            else:
                print('\n', data, end='')


    # def handle_comment(self, data):
    #     print('<!-- -->')

    # def handle_entityref(self, name):
    #     print('&%s;' % name)
    #
    # def handle_charref(self, name):
    #     print('&#%s;' % name)

def main():
    parser = MyHTMLParser()
    POS = './test-html.html'
    parser.feed(open(POS, 'r', encoding='utf-8').read())

if __name__ == '__main__':
    main()