from html.parser import HTMLParser
import requests as rq


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        for (key, value) in attrs:
            print(value)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
vnexpress = rq.request('GET', "https://vnexpress.net")
parser.feed(vnexpress.text)

print(parser.handle_starttag('h3', [('class', 'title_news')]))
