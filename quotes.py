#!/usr/bin/env python2.7
from urllib2 import urlopen
from bs4 import BeautifulSoup

def pull_quotes():
    quote_list = []
    page = urlopen('http://bash.org/?random').read().encode('utf-8')
    soup = BeautifulSoup(page, from_encoding="utf-8")
    for quote in soup.find_all("p", "qt"):
        quote_list.append(quote)
    quote_list.reverse()
    return quote_list

def get_new_quote(quotes):
    q = quotes.pop()
    return q.get_text().encode('utf-8')
