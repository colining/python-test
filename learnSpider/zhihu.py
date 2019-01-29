# -*- coding:utf-8 -*-
import requests

from pyquery import PyQuery


def demo_zhihu():
    headers = {'User-Agent': 'GoogleBot',
                'Host': 'www.zhihu.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    url = "https://www.zhihu.com/question/19942068"
    request = requests.get(url,headers = headers)
    # print request.text
    q = PyQuery(request.text)
    for each in q('.RichContent-inner>span.RichText.CopyrightRichText-richText').items():
        print each.html()
        print "\n"

def demo_csdn():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    url = 'http://my.csdn.net/my/mycsdn'
    cookies = {
        "uuid_tt_dd": "-5750057097675979193_20170813",
        "bdshare_firstime": "1502631250076",
        "UM_distinctid": "15deb00ed7f3cf-0d74fe6e19012f-70147079-1ee628-15deb00ed80326",
        "UserName": "qq_23974175",
        "UserInfo": "U994Tu8lY8pWLO09E6Fopx0yMjlt8i1l%2FSC2lOJlzbLpYu9rpy8ZuVdnsDFrqJWxCee3rAe1LI3Qst%2B4qIw8FR8exmLP7DxyJzfVSCzMeaeu6wIUrRbjWdBaAqeB2N48myPsz%2FT8c0FYOP1ig4BcPQ%3D%3D",
        "UserNick": "%E5%A2%A8%E5%9B%9E%E9%A6%96",
        "AU": "CC7",
        "UN": "qq_23974175",
        "UE": "746203216@qq.com",
        "BT": "1504683018949",
        "access-token": "41acfe90-cb01-4d17-ae5d-c2213367fb69",
        "Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac": "1504704570,1504713388,1504714359,1504715898",
        "Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac": "1504718480",
        "dc_tos=ovvc7m; dc_session_id": "1504702783089_0.8604081143913103"
    }
    r = requests.get(url, cookies=cookies, headers=headers)
    print r.text


if __name__ == '__main__':
    demo_zhihu()
    # demo_csdn()


