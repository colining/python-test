# coding:utf-8
import requests
from pyquery import PyQuery
import re
import urllib
import urllib2
import os
import sys
if __name__ == '__main__':
    imgurl = 'http://img.mmjpg.com/2017/1212/1.jpg'
    headers = {
                  'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
    'Accept - Encoding': 'gzip, deflate, sdch',
    'Accept - Language': 'zh - CN, zh;q = 0.8',
    'Cache - Control': 'max - age = 0',
    'Connection': 'keep - alive',
    'DNT': '1',
    'Host': 'img.mmjpg.com',
    'Referer': 'http: // www.mmjpg.com / mm / 1212',
    'Upgrade - Insecure - Requests': '1',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 53.0.2785.104 Safari / 537.36 Core / 1.53.3427.400 QQBrowser / 9.6.12513.400',
    }
    print imgurl
    r = requests.get(imgurl, headers = headers)
    print r.status_code
    with open("c:\\mymeizi\\test.jpg" , "wb") as code:
        code.write(r.content)