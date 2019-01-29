# -*- coding:utf-8 -*-
import requests
from pyquery import PyQuery
import re
import urllib

# def getImageUrl(list):
#     return

def downLoadImage():
# headers
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Host': 'pt.cugb.edu.cn',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
# cookie
    cookies = {'c_secure_uid': 'NTQ5', ' c_secure_pass': '7d72b685dccd03101b9f7eb6344f7c76', ' letskillie6': 'false',
               ' c_secure_user_link_online': 'success'}
# url
    url = 'http://pt.cugb.edu.cn/torrents.php'
# 请求
    r = requests.get(url, cookies, headers=headers, cookies=cookies)
    # print r.text
    q = PyQuery(r.text)

    #获取详情连接列表
    hrefList = list()
    for each in q('table.table-hover>tr>td:nth-child(2)>table>tr>td:nth-child(1)>a').items():
        hrefList.append(each.attr.href)
    x = 0
    for href in hrefList:
        r = requests.get("http://pt.cugb.edu.cn/"+href, cookies, headers=headers, cookies=cookies)
        # print r.text
        q = PyQuery(r.text)
        # print q('')
        for each in q('#main > table:nth-child(2) > tr> td.rowhead>a').items():
            reg = r'src="(.*?\.jpg)"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, each.html())
            print imglist[0]
            urllib.urlretrieve("http://pt.cugb.edu.cn"+imglist[0][0:], 'C:\imageSave/%s.jpg' % x)
            x +=1



def getTitle():
    # headers
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Host': 'pt.cugb.edu.cn',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    # cookie
    cookies = {'c_secure_uid': 'NTQ5', ' c_secure_pass': '7d72b685dccd03101b9f7eb6344f7c76', ' letskillie6': 'false',
               ' c_secure_user_link_online': 'success'}
    # url
    url = 'http://pt.cugb.edu.cn/torrents.php'
    # 请求
    r = requests.get(url, cookies, headers=headers, cookies=cookies)
    # 声明编码类型，防止乱码
    r.encoding = 'utf8'
    print r.text
    q = PyQuery(r.text)
    # 简单的获取首页的种子标题；
    # for each in q('table.table-hover>tr>td:nth-child(2)>table>tr>td:nth-child(1)>a>b:nth-last-child(1)').items():
    #     print each.html()
    #     print "\n"

if __name__ == '__main__':
    # downLoadImage()
    getTitle()

