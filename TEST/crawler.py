# _*_ coding: utf-8 _*_

# @Time     :2017.3.22 下午 8:26
# @Author   :ZuMing Shen
# File      :crawler.py
# software  :PyCharm
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read())
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not found")
else:
    print(title)